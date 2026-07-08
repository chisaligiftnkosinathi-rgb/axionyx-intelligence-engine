# ADR-0001: Why FastAPI?

Status
Accepted

Date
2026-07-08

Context
The Intelligence Engine required a framework that natively supported:
* Typed request and response models
* Automatic API documentation (OpenAPI/Swagger)
* Input validation
* Asynchronous capabilities for potentially high-latency epistemic checks
* Straightforward deployment in containerized environments

Decision
FastAPI was selected because it satisfies these requirements gracefully through native Python type hints, automatic Pydantic validation, zero-config OpenAPI generation, and full ASGI compatibility.

Alternatives Considered
* Flask: Lacks native async support and automatic OpenAPI generation without extensive plugins.
* Django: Too monolithic for a specialized epistemic validation microservice.
* Express (Node.js): Weak runtime type safety compared to Pydantic; previously caused build conflicts in the monorepo.
* Go / ASP.NET: Higher learning curve and less native ecosystem alignment with data science and validation libraries typically found in Python.

Consequences
Positive
* Rapid development velocity due to autocompletion and built-in docs.
* Mathematically rigorous request validation at the boundaries.
Negative
* Slightly heavier memory footprint than a minimal Go binary.

References
* FastAPI Documentation
