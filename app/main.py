from fastapi import FastAPI, Depends
from routes import auth
from dependencies import get_db_connection, get_current_user

app = FastAPI()

app.include_router(auth.auth_router, prefix="/auth")

@app.get("/users")
def get_users(
    conn = Depends(get_db_connection),
    current_user: dict = Depends(get_current_user)):
    return {
        "user_id": current_user.id,
        "email": current_user.email
    }