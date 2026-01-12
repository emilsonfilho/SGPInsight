from fastapi import FastAPI, Depends
from routes import auth, equipments
from dependencies import get_db_connection, get_current_user

app = FastAPI()

app.include_router(auth.auth_router, prefix="/auth")
app.include_router(equipments.router, prefix="/equipments")