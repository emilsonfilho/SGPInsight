from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config import settings
from database import conn

import os
import sqlite3

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def verify_password(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)

def get_password_hashed(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({ "exp": expire })
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas ou token expirado",
        headers={
            "WWW-Authenticate": "Bearer"
        },
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        email: str = payload.get("sub")
        user_id: int = payload.get("id")
        role_id: int = payload.get("role")
        
        if email is None:
            raise credentials_exception
        
        return {
            "email": email,
            "id": user_id,
            "role_id": role_id
        }
    except JWTError:
        raise credentials_exception

async def get_db_connection():
    conn.row_factory = sqlite3.Row
    
    return conn