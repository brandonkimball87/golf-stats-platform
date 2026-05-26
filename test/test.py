import sqlite3

DB_FILE = "golf_data.db" 

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM shots;")
    rows = cursor.fetchall()
    
    # print("\n--- DATABASE CONTENT ---")
    # for row in rows:
    #     print(row)
    # print("------------------------\n")
    print(rows)

except sqlite3.OperationalError as e:
    print(f"Could not read table: {e}")

finally:
    conn.close()