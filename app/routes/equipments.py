from fastapi import APIRouter, Depends
from enums import EquipmentStatusEnum, DepartmentEnum
from dependencies import get_db_connection, get_current_user
from repositories.equipment_repository import EquipmentRepository

router = APIRouter()

@router.get("/")
def get_equipments(
    status: EquipmentStatusEnum | None,
    department: DepartmentEnum | None,
    ean: str | None,
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return EquipmentRepository(conn).get()

    
