from Base import Base

from sqlalchemy import Integer, String, Boolean, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    
    username: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=False,
        index=True
    )
    
    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        index=True
    )
    
    hashed_password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    
    full_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    
    bio: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )
    
    profile_image_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="1"
    )
    
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default="0"
    )
    
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp()
    )
    
    last_login: Mapped[DateTime | None] = mapped_column(
        DateTime,
        nullable=True
    )
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
            "bio": self.bio
        }