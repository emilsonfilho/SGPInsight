from .base import Base
from typing import List, Optional
from datetime import datetime
from typing import Optional
from enums import MaintenanceStatusEnum
from schemas.user import Responsible
from schemas.equipment import Equipment

class MaintenanceCreate(Base):
    equipment_ids: List[str]
    description: str
    responsible_id: str

class Maintenance(Base):
    id: str
    description: str
    responsible_id: str # fazer a refatoração aqui
    created_at: datetime
    finished_at: Optional[datetime] = None

class MaintenanceResponse(Base):
    id: str
    description: str
    created_at: datetime
    finished_at: Optional[datetime] = None
    status: MaintenanceStatusEnum
    responsible: Responsible
    equipments_summary: List[Equipment] = []