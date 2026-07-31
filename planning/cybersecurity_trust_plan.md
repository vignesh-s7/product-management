# Trust & Security Plan: Reusable PO Skills

To build **absolute trust** for any GitHub user or cybersecurity team, we must keep this solution simple, fully transparent, and strictly compliant. We achieve this by abandoning complex shell scripts and relying entirely on **Declarative Markdown (`SKILL.md`)** that runs 100% locally.

## 1. Absolute Data Protection (GDPR, HIPAA, CCPA)
By keeping all execution local, we inherently comply with strict global data protection laws without needing overengineered architectures:
* **Zero Data Retention:** Skills process data in-memory and write locally. No data is sent to or stored on external servers.
* **No Profiling:** The AI will explicitly be instructed *not* to profile users, track usage, or retain metadata across sessions. 
* **Strict HIPAA/PII Handling:** Skills will include hard-coded guardrails instructing the AI: *"Do not extract, transmit, or log Protected Health Information (PHI) or Personally Identifiable Information (PII). Use only synthetic data for workflow generation."*

## 2. Eliminate Risk & "Excessive Agency"
Security teams flag `.sh` and `.bat` files because they can execute arbitrary code. We will remove this risk entirely:
* **No Executables:** Delete `orchestrate.sh`. All logic will be pure text instructions in `SKILL.md`.
* **Stateless Execution:** The AI acts as a workflow engine that only reads and writes text within the current project folder.
* **No Hidden Network Calls:** Skills will be explicitly banned from using curl, wget, or web search tools to prevent data exfiltration.

## 3. Transparent Trust (The "Trust Handshake")
To ensure users know they are safe, we will add straightforward documentation:
* **`SECURITY.md`:** A simple document outlining our Zero Data Retention, No Profiling, and strict Local Execution guarantees.
* **Immutable Releases:** We will sign all releases so users can cryptographically verify they haven't been tampered with.

**Summary:** We are not overengineering a security platform. We are building absolute trust by simply **doing less**—no scripts, no telemetry, no profiling, and zero external data storage.
