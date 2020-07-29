# -*- coding: utf-8 -*-

try:
    import func_files.config as config
    import func_files.database_commands as db_command
except ModuleNotFoundError:
    import config
    import database_commands as db_command

import psycopg2


class PGDatabaseMainExecutor:
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
        except Exception as e:
            print(e)
            return None

        return connection

    def close_connection_and_cursor(self, opened_connection, existing_cursor):
        existing_cursor.close()
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
        except Exception as e:
            print(e)

        self.close_connection_and_cursor(connection, cursor)

    def execute_read_query(self, query):
        if self.start_connection():
            connection = self.start_connection()
        else:
            return print("Execution is not possible! Bad connection")

        connection.autocommit = True
        result_info = ()
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result_info = cursor.fetchall()
        except Exception as e:
            print(e)

        self.close_connection_and_cursor(connection, cursor)

        return result_info


if __name__ == '__main__':
    db_info = config.pg_db_connection_info()
    db_executor = PGDatabaseMainExecutor(*db_info)

    print(db_executor.execute_read_query(db_command.insert_customer('name', '3456346', 34534)))

    print(db_executor.execute_read_query(db_command.select_customer_id_chat_id_from_customers()))

    # ("12.27.2020", "18:30", "name", "89104534545", CUSTOMER_ID)
