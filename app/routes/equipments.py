from fastapi import APIRouter, Depends, status
from enums import EquipmentStatusEnum, DepartmentEnum
from dependencies import get_db_connection, get_current_user
from repositories.equipment_repository import EquipmentRepository
from schemas.equipment import EquipmentCreate, Equipment, EquipmentMoveCreate, EquipmentMoveResponse
from typing import Optional, List

router = APIRouter()

@router.get("/", response_model=Optional[List[Equipment]])
def get_equipments(
    status: str | None = None,
    department: DepartmentEnum | None = None,
    ean: str | None = None,
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return EquipmentRepository(conn).get(ean, department, EquipmentStatusEnum.from_keyword(status))

    
@router.get("/{id}")
def get_equipment_by_id(equipment_id: str, conn = Depends(get_db_connection), user = Depends(get_current_user)):
    return EquipmentRepository(conn).get_by_id(equipment_id)

@router.post(
        "/", 
        response_model=Equipment,
        status_code=status.HTTP_201_CREATED
)
def create_equipment(equipment: EquipmentCreate, conn = Depends(get_db_connection), user = Depends(get_current_user)):
    return EquipmentRepository(conn).add(equipment)

@router.put("/{id}", response_model=Equipment)
def update_equipment(equipment_id: str, equipment: EquipmentCreate, conn = Depends(get_db_connection), user = Depends(get_current_user)):
    return EquipmentRepository(conn).update(equipment_id, equipment)

@router.post("/{id}/move", response_model=EquipmentMoveResponse)
def move_equipment(equipment_id: str, move: EquipmentMoveCreate, conn = Depends(get_db_connection), user = Depends(get_current_user)):
    return EquipmentRepository(conn).move(equipment_id, move)