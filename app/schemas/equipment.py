from .base import Base
from enums import EquipmentStatusEnum, DepartmentEnum

class Equipment(Base):
    id: str
    name: str
    ean: str
    equipment_status_id: str
    department_id: str

class EquipmentCreate(Base):
    name: str
    ean: str
    equipment_status_id: EquipmentStatusEnum
    department_id: DepartmentEnum