from schemas.equipment import Equipment
from psycopg2.extras import RealDictCursor

class EquipmentRepository:
    def __init__(self, connection):
        self.conn = connection
    
    def get(self):
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        cursor.exeucte("SELECT * FROM equipments")

        equipments = cursor.fetchall()

        if not row:
            return None
        
        return equipments