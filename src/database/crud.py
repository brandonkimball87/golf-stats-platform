from src.models.schemas import ShotInput
from src.database.connection import get_db_connection

def recommend_shot(rangefinder_distance: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    low_bound = rangefinder_distance - 10
    high_bound = rangefinder_distance + 10

    try:
        sql_query = """
            SELECT DISTINCT club 
            FROM shots 
            WHERE actual_distance BETWEEN ? AND ?
        """

        cursor.execute(sql_query, (low_bound, high_bound))

        rows = cursor.fetchall()

        clubs = [row[0] for row in rows]
        
        return clubs        
    
    except Exception as e:
        print(f"Database error details: {e}")
        return []
    
    finally:
        conn.close()



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
