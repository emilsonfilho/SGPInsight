from fastapi import APIRouter, Depends
from dependencies import get_db_connection, get_current_user
from repositories.component_repository import ComponentRepository

router = APIRouter()

@router.get("/")
def get_components(conn = Depends(get_db_connection), user = Depends(get_current_user)):
    return ComponentRepository(conn).get()