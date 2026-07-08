# API Reference

The AXIONYX Intelligence Engine is exposed via a FastAPI application.

## Core Endpoints

### `GET /health`
Validates the runtime health of the Intelligence Engine.
**Response:** `200 OK`

### `GET /docs`
The interactive Swagger UI for exploring the full OpenAPI specification. This is the recommended entry point for developers looking to integrate with the AIE.

### Evidence Ingestion (Proposed)
Future endpoints will adhere to the following semantic structure:
- `POST /api/v1/evidence/ingest`: Submit an Evidence Passport for validation and sealing.
- `GET /api/v1/evidence/{passport_id}`: Retrieve an immutable Evidence Passport.
- `GET /api/v1/replay/audit`: Trigger an epistemic replay simulation.
