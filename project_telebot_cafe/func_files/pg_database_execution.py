# import func_files.config as config

import psycopg2


class PGDataBaseExecutor:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def start_connection(self):
        try:
            connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except OperationalError as e:
            print(e)
            return None

        return connection

    def close_connection(self, opened_connection):
        opened_connection.close()

    def execute_query(self, query):
        if self.start_connection():
            connection = self.start_connection()
        else:
            return print("Execution is not possible! Bad connection")

        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except OperationalError as e:
            print(e)

        self.close_connection(connection)

    def execute_read_query(self, query):
        if self.start_connection():
            connection = self.start_connection()
        else:
            return print("Execution is not possible! Bad connection")

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result_info = cursor.fetchall()
        except OperationalError as e:
            print(e)

        self.close_connection(connection)

        return result_info


if __name__ == '__main__':
    pass
