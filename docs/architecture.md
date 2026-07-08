# Architecture

The AXIONYX architecture represents the evolution from a monolithic application into a mature, four-layer ecosystem of separated responsibilities.

## 4-Layer Ecosystem

1. **Research Layer**
   - Contains the Papers, Constitution, and the Scientific Information Architecture.

2. **Platform Layer (The Intelligence Engine)**
   - Deployed FastAPI backend.
   - Evidence Standards and core APIs.

3. **Applications Layer**
   - **iPhande:** Opportunities and community visibility.
   - **SANAS Explorer:** Laboratory and accreditation interfaces.
   - Future bespoke platforms.

4. **Demonstrations Layer**
   - Interactive UI demonstrators (Evidence Passports, Observatory, Scientific Workflows).

## Multi-Repository Strategy

To support this layered ecosystem, the AXIONYX codebase is physically distributed across specific repositories to preserve isolation:

### `axis_clean`
The primary research workspace. It contains the experimental scripts, original TypeScript monorepo packages, frontend UI demonstrators, and exploratory documentation.

### `axionyx-intelligence-engine` (This Repository)
The production-ready FastAPI service. It focuses purely on backend execution, deployment on Railway, and epistemic validation.

### `axionyx-contracts` (Future)
A shared schema registry. This will store the reusable TypeScript and Python contracts, models, and Evidence Specifications, allowing both `axis_clean` applications and the `Intelligence Engine` to safely share data structures.
