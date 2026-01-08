from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: str
    
    class Config:
        from_attributes = True