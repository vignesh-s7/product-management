# Security Policy

## Supported Versions

Currently, the `main` branch of `productowner-skill` is the only supported version for security updates.

| Version | Supported          |
| ------- | ------------------ |
| `main`  | :white_check_mark: |
| `< 1.0` | :x:                |

## Reporting a Vulnerability

We take the security of this Responsible AI Plugin Suite very seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to the repository maintainer.
Please include the following details in your report:
- A description of the vulnerability and its impact.
- Steps to reproduce the vulnerability (if applicable).
- Any potential mitigation or remediation steps.

You should receive a response within 48 hours acknowledging receipt of your vulnerability report. 

## Zero-Trust Architecture Note
This project operates as a declarative Markdown Swarm. It intentionally does not include shell scripts, Python dependencies, or external API calls. If you discover any mechanism within these `.md` files that allows for arbitrary code execution outside the bounds of the host AI agent, this is considered a critical security flaw and should be reported immediately.
