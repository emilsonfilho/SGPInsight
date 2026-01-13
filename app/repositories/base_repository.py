class BaseRepository:
    def _prepare_insert(self, data: dict):
        columns = list(data.keys())
        vals = list(data.values())

        cols = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))

        return cols, placeholders, vals

    def _prepare_update(self, data: dict):
        set_clauses = [f"{key} = %s" for key in list(data.keys())]
        set_str = ', '.join(set_clauses)

        vals = list(data.values())

        return set_str, vals
        