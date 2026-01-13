class RoleRepository:
    def __init__(self, connection):
        self.conn = connection
    
    def get(self):
        cursor = self.conn.cursor()

        try:
            query = """
                SELECT * FROM roles
            """

            cursor.execute(query)
            
            return cursor.fetchall()
        except Exception as e:
            raise e