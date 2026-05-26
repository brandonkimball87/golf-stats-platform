from src.models.schemas import ShotInput



try:
    ShotInput(club="7-iron", target_distance=150, actual_distance=152, accuracy="center")
    print("Success! Good shot data accepted.")
except Exception as e:
    print("Error:", e)