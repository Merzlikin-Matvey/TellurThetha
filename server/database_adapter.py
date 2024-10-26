import psycopg2

class Adapter:
    def __init__(self, url):
        self.conn = psycopg2.connect(url)
        self.cur = self.conn.cursor()

    def connect(self):
        return self.conn

    def select(self, table):
        request = f"""SELECT * FROM "{self.schema_name}"."{table}" """
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data

    def update(self, table, request, id):
        request_update = f"""UPDATE "{self.schema_name}"."{table}" SET {request} WHERE id={id}"""
        print(request_update)
        self.cursor.execute(request_update)
        self.conn.commit()

    def insert(self, table, data):
        request_insert = f"""INSERT INTO "{self.schema_name}"."{table}" ({",".join(list(data.keys()))}) VALUES ({",".join(list(data.items()))})"""
        self.cursor.execute(request_insert)
        self.conn.commit()

    def insert_batch(self, table, data, id_name):
        for row in data:
            for key, value in row.items():
                if isinstance(row[key], int):
                    row[key] = str(row[key])
                elif isinstance(row[key], str):
                    row[key] = f"'{row[key]}'"
        t = []
        for i in range(len(data)):
            names = f'"{'","'.join(list(data[i].keys()))}"'
            request_insert = f"""INSERT INTO "{self.schema_name}"."{table}" ({names}) VALUES ({",".join(list(data[i].values()))}) RETURNING {id_name} """
            print(request_insert)
            self.cursor.execute(request_insert)
        self.conn.commit()
        t = self.cursor.fetchall()
        return t

    def delete_all(self, table):
        request_delete = f"""DELETE FROM "{self.schema_name}"."{table}" WHERE 1=1"""
        self.cursor.execute(request_delete)
        self.conn.commit()

    # list_id = ['dimon'...]
    def delete_batch(self, table, list_id):
        for i in list_id:
            request_delete = f"""DELETE FROM "{self.schema_name}"."{table}" WHERE user_id = {i}"""
            self.cursor.execute(request_delete)
            print(request_delete)
        self.conn.commit()
