# ADR-0005: Why a Scientific Information Architecture?

Status
Accepted

Date
2026-07-08

Context
Scientific systems inherently involve observations, evidence, interpretation, governance, and institutional memory. Historically, these domains are often treated as isolated software components—where data storage, business logic, and scientific context are loosely coupled and easily fractured.

Decision
We explicitly adopted a Scientific Information Architecture (SIA) to unify these concerns. Rather than building a standard software application, we designed an adaptive computational architecture whose primary structural imperative is preserving the coherence of scientific evidence, provenance, and meaning.

Alternatives Considered
* Standard MVC (Model-View-Controller) Architecture: Too focused on application state rather than the provenance of knowledge.
* Data Lakes / Warehouses: Excellent for storage, but lacks the native computational governance and epistemic constraints required to prove truth.

Consequences
Positive
* Bridges the gap between academic research philosophy and executable software implementation.
* Ensures that the system's architecture inherently reflects its scientific mission.
Negative
* Requires a paradigm shift for traditional software engineers onboarding to the project.

References
* docs/scientific-information-architecture.md
* Christopher Alexander — The Nature of Order
