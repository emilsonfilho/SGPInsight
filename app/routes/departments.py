from fastapi import APIRouter, Depends
from dependencies import get_db_connection
from repositories.department_repository import DepartmentRepository

router = APIRouter()

@router.get("/")
def fetch_all_departments(conn = Depends(get_db_connection)):
    return DepartmentRepository(conn).get()