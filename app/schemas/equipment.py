from .base import Base

class Equipment(Base):
    id: str
    name: str
    ean: str
    equipment_status_id: str
    department_id: str