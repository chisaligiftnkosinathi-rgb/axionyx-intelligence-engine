from abc import ABC, abstractmethod
from typing import Dict, Optional
from .models import EvidencePassport

class EvidenceRepository(ABC):
    @abstractmethod
    def create(self, passport: EvidencePassport) -> None:
        pass
        
    @abstractmethod
    def get(self, passport_id: str) -> Optional[EvidencePassport]:
        pass

class InMemoryEvidenceRepository(EvidenceRepository):
    """
    An ephemeral in-memory adapter for Phase XIII demonstrations.
    Designed to be easily swapped for PostgresEvidenceRepository in the future.
    """
    def __init__(self):
        self._store: Dict[str, EvidencePassport] = {}
        
    def create(self, passport: EvidencePassport) -> None:
        self._store[passport.id] = passport
        
    def get(self, passport_id: str) -> Optional[EvidencePassport]:
        return self._store.get(passport_id)
