from .models import EvidencePassport
from .repositories import EvidenceRepository
from datetime import datetime
import json
import hashlib
import uuid

class EvidencePassportService:
    def __init__(self, repository: EvidenceRepository):
        self.repository = repository
        
    def _compute_canonical_hash(self, data: dict) -> str:
        """Computes a SHA-256 hash from a deterministic JSON representation."""
        canonical_json = json.dumps(data, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(canonical_json.encode('utf-8')).hexdigest()
        
    def create_passport(self, observation: dict) -> EvidencePassport:
        payload_hash = self._compute_canonical_hash(observation)
        passport_id = f"axid://evd/{payload_hash[:12]}-{uuid.uuid4().hex[:8]}"
        
        passport = EvidencePassport(
            id=passport_id,
            observation=observation,
            sha256_hash=payload_hash,
            created_at=datetime.utcnow().isoformat() + "Z",
            version="1.0",
            metadata={"issuer": "AXIONYX Intelligence Engine"}
        )
        self.repository.create(passport)
        return passport

    def get_passport(self, passport_id: str) -> EvidencePassport:
        return self.repository.get(passport_id)
        
    def verify_passport(self, passport_id: str) -> dict:
        passport = self.repository.get(passport_id)
        if not passport:
            return {"valid": False, "error": "Evidence Passport not found"}
            
        computed_hash = self._compute_canonical_hash(passport.observation)
        is_valid = computed_hash == passport.sha256_hash
        
        return {
            "valid": is_valid,
            "stored_hash": passport.sha256_hash,
            "computed_hash": computed_hash,
            "verified_at": datetime.utcnow().isoformat() + "Z"
        }
        
    def replay_passport(self, passport_id: str) -> dict:
        passport = self.repository.get(passport_id)
        if not passport:
            return {}
            
        return {
            "observation": passport.observation,
            "passport": passport.model_dump(),
            "provenance": [
                "Observation captured via REST API",
                "Payload canonicalized to strict deterministic JSON",
                f"SHA-256 hash computed: {passport.sha256_hash}",
                f"Passport sealed and issued identifier: {passport.id}",
                "Stored in immutable epistemic registry"
            ]
        }
