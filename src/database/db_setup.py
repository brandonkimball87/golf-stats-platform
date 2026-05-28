import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def run_query(self, sql, params=()):
        try:
            with self._get_connection() as conn:
                return pd.read_sql_query(sql, conn, params=params)
        except sqlite3.Error as e:
            print(f'Unable to execute the query: {e}')
            raise

    def execute_command(self, sql, params=()):
        try:
            with self._get_connection() as conn:
                conn.execute(sql, params)
                conn.commit()
        except sqlite3.Error as e:
            print(f'Database error occured: {e}')
            raise

    def refresh_table(self, refresh_table_name):
        drop_query = f'drop table if exists {refresh_table_name}'
        self.execute_command(sql = drop_query)

        create_query = f'''create table {refresh_table_name} (
                id integer primary key autoincrement,
                club text not null,
                target_distance integer not null,
                actual_distance integer not null,
                accuracy text not null,
                user text not null
                )'''
        self.execute_command(sql = create_query)
        print(f'Successfully refreshed table named {refresh_table_name}!')




    




# DB_FILE = "golf_data.db"

# def get_db_connection():
#     conn = sqlite3.connect(DB_FILE)
#     conn.row_factory = sqlite3.Row
#     return conn

