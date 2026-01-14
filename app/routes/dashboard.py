from fastapi import APIRouter, Depends
from dependencies import get_current_user, get_db_connection
from schemas.dashboard import DashboardResponse
from repositories.dashboard_repository import DashboardRepository

router = APIRouter()

@router.get("/stats", response_model=DashboardResponse)
def dashboard(user = Depends(get_current_user), conn = Depends(get_db_connection)):
    return DashboardRepository(conn).get()