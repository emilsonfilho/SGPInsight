from fastapi import APIRouter, Depends, status
from dependencies import get_current_user, get_db_connection
from repositories.alert_repository import AlertRepository
from schemas.alert import AlertCreate, AlertResponse

router = APIRouter()

@router.get("/")
def get_alerts(
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return AlertRepository(conn).get()

@router.post("/", response_model=AlertResponse, status_code=status.HTTP_201_CREATED)
def create_alert(
    alert: AlertCreate,
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return AlertRepository(conn).create(alert)