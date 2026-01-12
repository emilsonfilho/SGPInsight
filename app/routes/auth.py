from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from repositories.user_repository import UserRepository
from dependencies import verify_password, get_db_connection, create_access_token

auth_router = APIRouter()

@auth_router.post("/token")
async def login_for_acess_token(form_data: OAuth2PasswordRequestForm = Depends(), conn = Depends(get_db_connection)):
    user = UserRepository(conn).login(form_data)
    
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="E-mail ou senha inválidos!")
    
    if user.disabled:
        raise HTTPException(status_code=400, detail="Usuário inativo!")
    
    access_token = create_access_token(
        data={
            "sub": user.email,
            "id": user.id,
            "role": user.role_id
        }
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
