from fastapi import APIRouter, Depends, status
from dependencies import get_db_connection, get_current_user
from repositories.maintenance_repository import MaintenanceRepository
from enums import MaintenanceStatusEnum
from schemas.maintenance import MaintenanceCreate, Maintenance

router = APIRouter()

@router.get("/")
def get_maintenances(
    status: str | None = None,
    responsible_id: str | None = None,
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return MaintenanceRepository(conn).get(MaintenanceStatusEnum.from_keyword(status), responsible_id)

@router.post(
        "/",
        response_model=Maintenance,
        status_code=status.HTTP_201_CREATED
)
def create_maintenance(
    maintenance: MaintenanceCreate, 
    conn = Depends(get_db_connection), 
    user = Depends(get_current_user)
):
    return MaintenanceRepository(conn).add(maintenance)

@router.post(
        "/{id}/finish",
        response_model=Maintenance
)
def finish_maintenance(
    maintenance_id: str, 
    conn = Depends(get_db_connection), 
    user = Depends(get_current_user)
):
    return MaintenanceRepository(conn).finish(maintenance_id)