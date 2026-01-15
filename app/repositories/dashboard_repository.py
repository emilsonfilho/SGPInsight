from .base_repository import BaseRepository
from schemas.dashboard import DashboardResponse

class DashboardRepository(BaseRepository):
    def __init__(self, connection):
        self.conn = connection

    def get(self):
        cursor = self.conn.cursor()

        try:
            sql = "SELECT * FROM vw_dashboard_stats"

            cursor.execute(sql)
            data = cursor.fetchone()
            return DashboardResponse(**data)
        except Exception as e:
            raise e