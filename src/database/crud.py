from src.models.schemas import ShotInput
from src.database.connection import get_db_connection

def create_shot(shot: ShotInput):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        sql_query = """
            insert into shots (club, target_distance, actual_distance, accuracy)
            values (?, ?, ?, ?)
        """
        cursor.execute(sql_query, (
            shot.club, 
            shot.target_distance, 
            shot.actual_distance, 
            shot.accuracy
        ))
        conn.commit()
        return True
    
    except Exception as e:
        print(f"Database error details: {e}")
        return False
    
    finally:
        conn.close()