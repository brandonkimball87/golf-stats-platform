from shot_queries import ShotService

qry = ShotService('golf_data.db')

shot = {
    'club': '9-iron',
    'target_distance': 130,
    'actual_distance': 126,
    'accuracy': 'center',
    'user': 'isabella'
}

qry.upload_shot_to_db(
    shot_data = shot,
    table = 'shots')


# result = qry.get_all_shots(table='shots', user='isabella')
# print(result)