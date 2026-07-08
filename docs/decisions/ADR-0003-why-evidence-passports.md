# ADR-0003: Why Evidence Passports?

Status
Accepted

Date
2026-07-08

Context
Traditional CRUD (Create, Read, Update, Delete) systems typically prioritize representing current state. However, the AXIONYX platform specifically requires preserving provenance, lineage, and reproducibility. If state is overwritten, the historical context of how a scientific or institutional conclusion was reached is permanently lost.

Decision
We adopted cryptographically sealed Evidence Passports as the atomic unit of truth. Instead of mutating a database record, the system generates sequential Evidence Passports. 

Alternatives Considered
* Standard Relational DB (PostgreSQL mutations): Fails to preserve historical state natively without complex audit tables.
* Event Sourcing / Kafka: Preserves history, but can be highly complex to query without materializing views, and does not inherently provide cryptographic sealing of individual payloads for external verification.
* Blockchain: Provides immutability but introduces unacceptable latency, cost, and complexity for institutional scientific data.

Consequences
Positive
* Total provenance and reproducibility.
* Enables flawless epistemic replay and auditability.
* Passports can be verified externally by third parties.
Negative
* Increased storage requirements as data is never deleted, only appended.
* Requires specialized replay logic to determine the "current" state.

References
* AXIONYX Evidence Passport Specification
