class BaseRepository:
    def _prepare_insert(self, data: dict):
        columns = list(data.keys())
        vals = list(data.values())

        cols = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))

        return cols, placeholders, vals
        