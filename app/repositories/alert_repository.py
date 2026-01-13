class AlertRepository:
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
            
            cursor.execute(sql)

            return cursor.fetchall()
        except Exception as e:
            raise e