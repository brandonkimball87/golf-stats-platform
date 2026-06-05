from src.database.db_setup import DatabaseManager

class ShotService:
    def __init__(self, db_path='golf_data.db'):
        self.db = DatabaseManager(db_path)

    def get_all_shots(self, user=None, table_name='shots'):
        query = f'''select * from {table_name}'''
        params = ()
        if user:
            query += ''' where user = ?'''
            params = (user,)
        result = self.db.run_query(sql = query, params = params)
        return result
    
    def get_unique_users(self, table_name='shots'):
        query = f'''select distinct user from {table_name}'''
        params = ()
        result = self.db.run_query(sql = query, params = params)
        return result

    def upload_shot_to_db(self, shot_data, table_name='shots'):
        query = f'''insert into {table_name} (club, target_distance, actual_distance, accuracy, user) 
                values (?, ?, ?, ?, ?)'''
        params = (
            shot_data.club, 
            shot_data.target_distance, 
            shot_data.actual_distance, 
            shot_data.accuracy,
            shot_data.user
            )
        self.db.execute_command(sql = query, params=params)
        print(f'''{shot_data.user}, sucesfully uploaded your {shot_data.actual_distance} yard {shot_data.club} shot into the {table_name} table!''')
        return True