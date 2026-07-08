# ADR-0002: Why Railway?

Status
Accepted

Date
2026-07-08

Context
The project required a deployment platform that could guarantee zero-downtime rollouts, reproducible builds, and seamless GitHub integration, while abstracting away the operational complexity of managing bare-metal servers or Kubernetes clusters during the research phase.

Decision
Railway was selected because it met the project's deployment requirements at this stage. Specifically, its use of Nixpacks allows for deterministic OCI container builds straight from a `requirements.txt` and a `railway.toml`, bypassing the need to maintain a custom Dockerfile.

Alternatives Considered
* Docker on VPS: Requires manual provisioning, SSL management, and pipeline setup.
* Render / Fly.io: Viable alternatives, but Railway's current buildpack engine (Nixpacks) provided the most reliable parsing for our specific Python/FastAPI environment.
* Kubernetes / AWS / Azure: Too operationally complex for the current stage of the project; introduces unnecessary infrastructure overhead.

Consequences
Positive
* Near-instant deployments from `git push`.
* Abstracted infrastructure allows the team to focus on scientific architecture.
Negative
* Vendor lock-in to Railway's specific Nixpack heuristics, though migration to a standard Dockerfile is trivial if needed in the future.

References
* Railway Documentation
* Nixpacks Architecture
