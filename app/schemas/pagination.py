from .base import Base

class Pagination(Base):
    page: int
    per_page: int
    total_records: int