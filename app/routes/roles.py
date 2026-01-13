from fastapi import APIRouter, Depends
from dependencies import get_db_connection
from repositories.role_repository import RoleRepository

router = APIRouter()

@router.get("/")
def fetch_all_departments(conn = Depends(get_db_connection)):
    return RoleRepository(conn).get()