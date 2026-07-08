# ADR-0006: API Versioning Strategy

Status
Accepted

Date
2026-07-08

Context
As the AXIONYX Intelligence Engine matures from a research prototype into a robust production platform, multiple independent client applications (e.g., `axionyx-demos`, ChemIS, iPhande) will increasingly depend on its REST API. Without a formal versioning strategy, evolving the Evidence Passport payload structure or epistemic replay mechanics could silently break downstream clients and corrupt institutional workflows.

Decision
We will enforce explicit URI-based API versioning for all programmatic contracts.

1.  **URI Structure:** Every API endpoint must be prefixed with `/api/v{major}` (e.g., `/api/v1/evidence/passports`).
2.  **Backwards Compatibility:** The core payload structures for a given major version (e.g., `v1`) are immutable. We will not remove fields, rename endpoints, or alter response shapes in a way that breaks existing clients.
3.  **Breaking Changes (v2):** If the Scientific Information Architecture demands a fundamentally new paradigm for Evidence Passports (e.g., a shift from SHA-256 to quantum-resistant hashing, or a completely different provenance chain schema), this constitutes a breaking change. A new `/api/v2/` namespace will be created, allowing `v1` and `v2` to run concurrently until clients migrate.
4.  **Response Metadata:** Every API response must include an `api_version` field in its root metadata wrapper to programmatically guarantee the client is parsing the expected contract.

Alternatives Considered
*   Header-based Versioning (e.g., `Accept: application/vnd.axionyx.v1+json`): More REST-compliant, but harder to discover, document via OpenAPI, and debug in a browser or CLI environment compared to clear URI prefixes.
*   No Versioning (Continuous Evolution): Unacceptable for a governance and evidence engine where exact epistemic replay relies on strict structural determinism.

Consequences
Positive
*   Guarantees stability for institutional partners and diverse frontends.
*   Allows the backend architecture to evolve safely without disrupting live demonstrations.
*   Reinforces the concept of the Intelligence Engine as a reliable, invariant source of truth.
Negative
*   Requires maintaining concurrent logic if multiple major versions are supported simultaneously.

References
*   [API Reference](../api.md)
