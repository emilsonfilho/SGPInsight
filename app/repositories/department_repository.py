class DepartmentRepository:
    def __init__(self, connection):
        self.conn = connection

    def get(self):
        cursor = self.conn.cursor()

        try:
            query = """
                SELECT d.*, u.firstname
                FROM departments d
                JOIN users u ON d.responsible_id = u.id
            """

            cursor.execute(query)
            
            return cursor.fetchall()
        except Exception as e:
            raise e