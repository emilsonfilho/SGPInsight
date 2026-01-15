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

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_alert(id: str, conn = Depends(get_db_connection), user = Depends(get_current_user)):
    success = AlertRepository(conn).delete(id)
    
    if not success:
        # Se tentou apagar algo que não existe, retorna 404
        raise HTTPException(status_code=404, detail="Alerta não encontrado")
    
    # Retorna nada (204) pois o recurso deixou de existir
    return