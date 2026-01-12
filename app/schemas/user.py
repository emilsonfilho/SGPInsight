from .base import Base

class UserLogin(Base):
    id: str
    firstName: str
    lastName: str
    email: str
    role_id: str
    password: str
    disabled: bool