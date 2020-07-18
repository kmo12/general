# -*- coding: utf-8 -*-

import config
import database_commands as db_command

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
    db_executor = PGDataBaseExecutor(db_info[0],  # database
                                     db_info[1],  # user
                                     db_info[2],  # password
                                     db_info[3],  # host
                                     db_info[4],  # port
                                     )

    print(db_command.test_create_user("Михаил", "89104534545"))

    print(db_command.test_create_reservation("12.27.2020",
                                             "18:30",
                                             "Михаил",
                                             "89104534545",
                                             1))

    db_executor.execute_query(db_command.test_create_user("Михаил", "89104534545"))

    db_executor.execute_query(db_command.test_create_reservation("12.27.2020",
                                                                 "18:30",
                                                                 "Михаил",
                                                                 "89104534545",
                                                                 1))
