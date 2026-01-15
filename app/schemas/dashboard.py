from .base import Base
from typing import List
from .equipment import EquipmentStatus
from .department import Department
from .maintenance import Maintenance
from.user import Responsible
from enums import EquipmentStatusEnum, DepartmentEnum
from pydantic import field_validator
from datetime import datetime

class DashboardSummary(Base):
    total_equipments: int
    total_active_maintenances: int
    equipment_health_rate: str

class DashboardCount(Base):
    count: int

class DashboardEquipments(DashboardCount):
    status: EquipmentStatus

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

class DashboardDepartments(DashboardCount):
    department: Department

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

class DashboardMaintenance(Base):
    id: str
    description: str
    created_at: datetime
    days_open: int
    responsible: Responsible

class DashboardMaintenances(Base):
    active_count: int
    avg_days_open: float
    opened_list: List[DashboardMaintenance] = []

class DashboardResponse(Base):
    summary: DashboardSummary
    equipments_by_status: List[DashboardEquipments] = []
    equipments_by_department: List[DashboardDepartments] = []
    maintenance_overview: DashboardMaintenances