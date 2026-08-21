"""Secure allowlisted terminal command executor — Story 04.2.

Runs exactly one of three local validation commands and returns captured output.
No arbitrary shell access. Allowlist enforced before subprocess spawn.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ALLOWED_COMMANDS: frozenset[str] = frozenset({"validate", "test", "compile"})
_TIMEOUT_SECONDS = 30
_MAX_OUTPUT_BYTES = 65536  # 64 KB


class TerminalExecService:
    """Runs allowlisted local commands and returns stdout/stderr."""

    def __init__(self, root: Path) -> None:
        self._root = Path(root)

    def exec(self, command: str) -> dict[str, Any]:
        if not isinstance(command, str) or command not in ALLOWED_COMMANDS:
            raise ValueError(
                f"command not in allowlist: {command!r}. "
                f"Allowed: {sorted(ALLOWED_COMMANDS)}"
            )
        layer_a = str(self._root / "layer_a.py")
        test_file = str(self._root / "test_layer_a.py")
        build_file = str(self._root / "layer_a_build.py")
        terminal_file = str(self._root / "layer_a_terminal.py")
        if command == "validate":
            cmd = [sys.executable, layer_a, "validate"]
        elif command == "test":
            cmd = [
                sys.executable,
                "-W", "error::ResourceWarning",
                "-m", "unittest", "-v",
            ]
        else:
            cmd = [
                sys.executable, "-m", "py_compile",
                layer_a, test_file, build_file, terminal_file,
            ]
        try:
            # Bytecode goes to a throwaway dir. The platform default can be an
            # unwritable OS cache path, which fails the run for a reason that has
            # nothing to do with the code being checked.
            with tempfile.TemporaryDirectory(prefix="pi-pycache-") as cache_dir:
                result = subprocess.run(
                    cmd,
                    cwd=str(self._root),
                    capture_output=True,
                    timeout=_TIMEOUT_SECONDS,
                    env={**os.environ, "PYTHONPYCACHEPREFIX": cache_dir},
                )
            stdout_bytes = result.stdout[:_MAX_OUTPUT_BYTES]
            stderr_cap = _MAX_OUTPUT_BYTES - len(stdout_bytes)
            stderr_bytes = result.stderr[:stderr_cap]
            truncated = (
                len(result.stdout) > _MAX_OUTPUT_BYTES
                or len(result.stderr) > stderr_cap
            )
            return {
                "status": "PASS" if result.returncode == 0 else "FAIL",
                "command": command,
                "returncode": result.returncode,
                "stdout": stdout_bytes.decode("utf-8", errors="replace"),
                "stderr": stderr_bytes.decode("utf-8", errors="replace"),
                "truncated": truncated,
            }
        except subprocess.TimeoutExpired:
            return {
                "status": "TIMEOUT",
                "command": command,
                "returncode": -1,
                "stdout": "",
                "stderr": f"Command timed out after {_TIMEOUT_SECONDS}s.",
                "truncated": False,
            }
