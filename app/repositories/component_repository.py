class ComponentRepository:
    def __init__(self, connection):
        self.conn = connection
    
    def get(self):
        cursor = self.conn.cursor()

        try:
            cursor.execute("SELECT * FROM components")

            return cursor.fetchall()
        except Exception as e:
            raise e