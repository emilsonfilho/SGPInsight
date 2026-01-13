from .base import Base
from typing import List, Optional
from datetime import datetime

class MaintenanceCreate(Base):
    equipment_ids: List[str]
    description: str
    responsible_id: str

class Maintenance(Base):
    id: str
    description: str
    responsible_id: str
    created_at: datetime
    finished_at: Optional[datetime] = None