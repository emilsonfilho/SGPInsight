from .base import Base
from enums import EquipmentStatusEnum, DepartmentEnum
from pydantic import field_validator
from schemas.department import Department
from schemas.pagination import Pagination
from typing import List, TYPE_CHECKING, Optional
from datetime import datetime

class EquipmentBase(Base):
    name: str
    ean: str

class EquipmentStatus(Base):
    id: str
    name: str

class Equipment(EquipmentBase):
    id: str
    status: EquipmentStatus
    department: Department

    @field_validator('status', mode='before')
    @classmethod
    def format_status(cls, v):
        if isinstance(v, str):
            try:
                enum_obj = EquipmentStatusEnum(v)

                return EquipmentStatus(
                    id=enum_obj.value,
                    name=enum_obj.label
                )
            except ValueError:
                return EquipmentStatus(
                    id=v,
                    name="Status Desconhecido"
                )
        return v
    
    @field_validator('department', mode='before')
    @classmethod
    def format_department(cls, v):
        if isinstance(v, str):
            try:
                enum_obj = DepartmentEnum(v)

                return Department(
                    id=enum_obj.value,
                    name=enum_obj.label
                )
            except ValueError:
                return Department(
                    id=v,
                    name="Departamento Desconhecido"
                )
        return v
        

class EquipmentCreate(EquipmentBase):
    equipment_status_id: EquipmentStatusEnum
    department_id: DepartmentEnum    

class EquipmentMoveCreate(Base):
    newly_alocated_at: DepartmentEnum

class EquipmentMoveResponse(Base):
    id: str
    equipment_id: str
    previously_located_at: DepartmentEnum # acho que vai precisar de uma refatoração aqui para que ele converta o ID em objeto
    newly_alocated_at: DepartmentEnum

class MaintenanceForHistory(Base):
    id: str
    description: str
    responsible_id: str # fazer a refatoração aqui
    created_at: datetime
    finished_at: Optional[datetime] = None

class EquipmentMoveWithDate(EquipmentMoveResponse): # tem que refatorar isso daqui para que o outro passe a data também porque é importante
    date: datetime

class HistoryTimeline(Base):
    movements: List[EquipmentMoveWithDate] = []
    maintenances: List[MaintenanceForHistory] = []

class EquipmentHistoryResponse(Base):
    equipment_summary: Equipment
    pagination: Pagination
    history_timeline: HistoryTimeline