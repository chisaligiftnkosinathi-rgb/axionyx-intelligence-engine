from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import json
import os
from pathlib import Path

app = FastAPI(title="AXIS Evidence Governance API")

# Setup CORS to allow the Next.js frontend to interact with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For demonstration, allow all. Hardened in prod.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

@app.get("/health")
def health_check():
    return {"status": "operational", "system": "AXIS_Governance_Engine"}

@app.get("/registry")
def get_registry():
    registry_path = BASE_DIR / "registry" / "evidence_registry.json"
    if not registry_path.exists():
        raise HTTPException(status_code=404, detail="Registry index not found")
    with open(registry_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/passport/{axid:path}")
def get_passport(axid: str):
    # Search the registry for the passport file location based on AXID
    registry_path = BASE_DIR / "registry" / "evidence_registry.json"
    if not registry_path.exists():
        raise HTTPException(status_code=404, detail="Registry index not found")
        
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)
        
    for p in registry.get("passports", []):
        if p["axid"] == axid or p["axid"] == f"axid://{axid}":
            # For this prototype, we'll return the zip file itself if it exists,
            # or we might need to return the passport JSON metadata.
            # Usually an Evidence Passport is an .axispack (ZIP)
            # Let's see if we have an .axispack file locally that matches.
            # We hardcode the path to the prototype axispack for the coal sample.
            axispack_path = BASE_DIR / "COAL_SAMPLE_2026_00001.axispack" 
            if not axispack_path.exists():
                 # fallback check in demonstrator package
                 axispack_path = BASE_DIR / "AXIS_Demonstrator_v1" / "Demonstration" / "COAL_SAMPLE_2026_00001.axispack"
                 
            if axispack_path.exists():
                return FileResponse(
                    path=axispack_path,
                    media_type="application/zip",
                    filename="COAL_SAMPLE_2026_00001.axispack"
                )
            else:
                 return {"status": "not_found", "message": "The .axispack container is currently offline."}
                 
    raise HTTPException(status_code=404, detail="Evidence Passport not found in registry")

@app.get("/classes")
def get_classes():
    return {
        "classes": [
            {"class": "EP-001", "name": "Research Proposal", "purpose": "A governed declaration of research intent, methodology, and ethics."},
            {"class": "EP-002", "name": "Laboratory Result", "purpose": "An analytical artifact mapping experimental data and sample metrics."},
            {"class": "EP-003", "name": "Inspection Evidence", "purpose": "Field or facility inspection technical records."},
            {"class": "EP-004", "name": "Calibration Record", "purpose": "Traceability and calibration data for analytical instruments."},
            {"class": "EP-005", "name": "Compliance Evidence", "purpose": "System-level audit trails and conformity assessments."}
        ]
    }

@app.get("/constitution")
def get_constitution():
    constitution_path = BASE_DIR / "constitutions" / "axionyx_evidence_standard_v1.json"
    if not constitution_path.exists():
        raise HTTPException(status_code=404, detail="Constitution not found")
    with open(constitution_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/architecture")
def get_architecture():
    # Return the structure mapping for the Next.js visualizer
    return {
        "infrastructure": {
            "name": "AXIS Computational Governance",
            "layers": [
                {"name": "Governance Layer", "components": ["Constitution Engine", "Canonical Governance Graph"]},
                {"name": "Trust Layer", "components": ["Evidence Passport", "Cryptographic Hash"]},
                {"name": "Identity Layer", "components": ["AXID Resolver", "Evidence Registry"]}
            ]
        }
    }
