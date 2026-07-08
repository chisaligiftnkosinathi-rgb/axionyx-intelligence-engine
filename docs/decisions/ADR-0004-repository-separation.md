# ADR-0004: Repository Separation Strategy

Status
Accepted

Date
2026-07-08

Context
The AXIONYX ecosystem was originally housed in a single monorepo (`axis_clean`) that contained:
* Python backend services
* TypeScript React applications
* Research documentation
* Deployment configurations

This led to severe deployment complexity. Automated build systems (like Railway's Nixpacks) encountered mixed responsibilities and build ambiguity, often triggering Node.js builds for Python services, resulting in deployment failures (e.g., 502 Bad Gateway).

Decision
We separated the ecosystem into distinct, purpose-driven repositories to cleanly decouple responsibilities:

1. `axis_clean`: The research workspace, containing experiments, UI demonstrators, and exploratory documentation.
2. `axionyx-intelligence-engine`: The production FastAPI runtime, strictly isolated to Python and backend epistemic validation.
3. `axionyx-contracts` (Future): Shared schemas, TypeScript/Python models, and evidence specifications to bridge the frontends and backends safely.

Alternatives Considered
* Enforcing strict monorepo tooling (Turborepo/Nx with custom Dockerfiles): Considered, but the overhead of maintaining custom build pipelines for disparate languages outweighed the benefits during this rapid evolution phase.

Consequences
Positive
* Simplified, deterministic deployments for the backend.
* Clear cognitive boundaries for developers and researchers.
Negative
* Requires synchronizing shared contracts across repositories (mitigated by the future `axionyx-contracts` repo).

References
* Deployment Failure Post-Mortem (Phase X)
