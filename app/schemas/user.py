from .base import Base
from schemas.role import RoleOut
from enums import RoleEnum
from pydantic import field_validator

class UserLogin(Base):
    id: str
    firstname: str
    lastname: str
    email: str
    role_id: str
    password: str
    disabled: bool 

class Responsible(Base):
    id: str
    full_name: str
    role: RoleOut
    
    @field_validator('role', mode='before')
    @classmethod
    def format_role(cls, v):
        if isinstance(v, str):
            try:
                enum_obj = RoleEnum(v)
                return RoleOut(
                    key=enum_obj.name,
                    id=enum_obj.value,
                    label=enum_obj.label
                )
            except ValueError:
                # Retorna um objeto genérico para não quebrar a API
                return RoleOut(
                    key="UNKNOWN_ROLE",
                    id=v,
                    label="Cargo Desconhecido"
                )
        
        return v