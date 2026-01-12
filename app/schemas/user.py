from .base import Base

class UserLogin(Base):
    id: str
    firstname: str
    lastname: str
    email: str
    role_id: str
    password: str
    disabled: bool