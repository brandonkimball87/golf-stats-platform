from src.database.crud import shot_history

def rec_club_average_distance(rangefinder_distance):
    
    if not isinstance(rangefinder_distance, int):
        raise TypeError(f"Distance must be a whole number, not a {type(rangefinder_distance).__name__}.")

    elif rangefinder_distance <= 0:
        raise ValueError("Distance must be a positive number greater than zero.")

    elif rangefinder_distance > 300:
        raise ValueError(f"{rangefinder_distance} yards is too far! Please enter a distance under 300 yards.")

    result = shot_history()
    if result.empty:
        raise LookupError("You haven't logged any shots yet! Go track a few shots first.") 

    distribution = result.groupby('club')['actual_distance'].mean().round(0)
    distribution = distribution.reset_index(name='average_distance')

    closest_distance_idx = (distribution['average_distance'] - rangefinder_distance).abs().idxmin()
    club_suggestion = distribution.loc[closest_distance_idx, 'club']
    str(club_suggestion[0])

    return club_suggestion

# result = rec_club_average_distance(192)
# print(result)

# 150 is 8-iron, 144 is 6-iron