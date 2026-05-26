import sqlite3

DB_FILE = "golf_data.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            club TEXT NOT NULL,
            target_distance INTEGER NOT NULL,
            actual_distance INTEGER NOT NULL,
            accuracy TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()