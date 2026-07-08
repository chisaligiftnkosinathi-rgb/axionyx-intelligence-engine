from pydantic import BaseModel
from typing import Dict, Any, List

class EvidencePassport(BaseModel):
    id: str
    observation: Dict[str, Any]
    sha256_hash: str
    created_at: str
    version: str
    metadata: Dict[str, Any]

class APIResponse(BaseModel):
    api_version: str = "1.0"
    engine: str = "AXIONYX Intelligence Engine"
    status: str
    data: Dict[str, Any]
