from fastapi import APIRouter, Depends
from dependencies import get_db_connection, get_current_user
from repositories.maintenance_repository import MaintenanceRepository
from enums import MaintenanceStatusEnum

router = APIRouter()

@router.get("/")
def get_maintenances(
    status: str | None = None,
    responsible_id: str | None = None,
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return MaintenanceRepository(conn).get(MaintenanceStatusEnum.from_keyword(status), responsible_id)