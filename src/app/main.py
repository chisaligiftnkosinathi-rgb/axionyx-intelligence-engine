from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

from .models import APIResponse
from .repositories import InMemoryEvidenceRepository
from .services import EvidencePassportService

app = FastAPI(title="AXIONYX Intelligence Engine", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize singletons (to be replaced by dependency injection in prod)
repo = InMemoryEvidenceRepository()
passport_service = EvidencePassportService(repository=repo)

def build_response(status: str, data: Dict[str, Any]) -> dict:
    return APIResponse(status=status, data=data).model_dump()


@app.get("/health")
def health_check():
    return {"status": "operational", "system": "AXIONYX Intelligence Engine"}

# ---------------------------------------------------------
# Evidence Passport API (v1)
# ---------------------------------------------------------

@app.post("/api/v1/evidence/passports")
def create_passport(observation: Dict[str, Any]):
    passport = passport_service.create_passport(observation)
    return build_response("sealed", {
        "passport_id": passport.id,
        "hash": passport.sha256_hash,
        "created_at": passport.created_at,
        "status": "sealed"
    })

@app.get("/api/v1/evidence/passports/{passport_id:path}")
def get_passport(passport_id: str):
    passport = passport_service.get_passport(passport_id)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")
    return build_response("success", passport.model_dump())

@app.post("/api/v1/evidence/passports/{passport_id:path}/verify")
def verify_passport(passport_id: str):
    result = passport_service.verify_passport(passport_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return build_response("success", result)

@app.get("/api/v1/evidence/passports/{passport_id:path}/replay")
def replay_passport(passport_id: str):
    result = passport_service.replay_passport(passport_id)
    if not result:
        raise HTTPException(status_code=404, detail="Passport not found")
    return build_response("success", result)
