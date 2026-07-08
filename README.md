# AXIONYX Intelligence Engine (AIE)
*An adaptive scientific information architecture for evidence, provenance, replay, and institutional memory.*

## What is AXIONYX?
The AXIONYX Intelligence Engine (AIE) is the core computational foundation for the ChemIS platform. It applies the principles of Scientific Information Architecture (SIA) to establish a verifiable, decentralized, and human-centered truth engine. It does not dictate truth, but preserves the evidence and provenance required to audit and reconstruct truth deterministically.

## Why does it exist?
AXIONYX exists to solve the crisis of reproducibility, transparency, and trust in institutional science and governance. By treating evidence preservation as a structural requirement rather than an afterthought, the engine provides a robust framework where computational truth is structurally constrained by evidence.

## Architecture
AXIONYX is structured as a scalable FastAPI backend that handles epistemic truth validation, graph-based demand engines, and cryptographic Evidence Passports.
- See [Architecture](docs/architecture.md) for system design.
- See [Scientific Information Architecture](docs/scientific-information-architecture.md) for philosophical foundations.
- See [The Codex](docs/codex.md) for governance and stewardship models.

## Quick Start
To run the Intelligence Engine locally:
```bash
pip install -r requirements.txt
uvicorn src.app.main:app --reload
```

## Deployment
AXIONYX is designed for zero-config deployment on Railway using Nixpacks.
See [Deployment](docs/deployment.md) for details on the `railway.toml` configuration.

## Documentation Reference
- [Architecture & Decisions](docs/architecture.md)
- [Evidence Passports](docs/evidence-passports.md)
- [API Reference](docs/api.md)
- [Governance](docs/governance.md)
- [Research Roadmap](docs/research-roadmap.md)

## Citation
If you use the AXIONYX Intelligence Engine in your research, please cite the foundational SIA documents and acknowledge the Codex structure.

## License
All Rights Reserved (2026) - ChemIS Research Programme
