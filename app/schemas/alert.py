from .base import Base
from datetime import datetime

class AlertCreate(Base):
    description: str
    equipment_id: str 
    priority_id: str
    origin: str = "Manual"

class AlertResponse(Base):
    id: str
    description: str
    created_at: datetime