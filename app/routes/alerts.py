from fastapi import APIRouter, Depends
from dependencies import get_current_user, get_db_connection
from repositories.alert_repository import AlertRepository

router = APIRouter()

@router.get("/")
def get_alerts(
    conn = Depends(get_db_connection),
    user = Depends(get_current_user)
):
    return AlertRepository(conn).get()