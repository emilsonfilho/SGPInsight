from schemas.alert import AlertCreate
from .base_repository import BaseRepository

class AlertRepository(BaseRepository):
    def __init__(self, connection):
        self.conn = connection
    
    def get(self):
        cursor = self.conn.cursor()

        try:
            query = """
                "SELECT a.id, description, origin, equipment_id, name as priority
                FROM alerts a
                JOIN alert_priority ap ON priority_id = ap.id
                ORDER BY priority_id DESC"
            """
            
            cursor.execute(query)

            return cursor.fetchall()
        except Exception as e:
            raise e

    def create(
            self,
            alert_data: AlertCreate
    ):
        cursor = self.conn.cursor()

        try:
            data = alert_data.model_dump(exclude_unset=True)

            cols, placeholders, vals = self._prepare_insert(data)

            sql = f"""
                INSERT INTO alerts
                ({cols})
                VALUES
                ({placeholders})
                RETURNING *
            """
        
            cursor.execute(sql, vals)

            self.conn.commit()

            return cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            raise e
