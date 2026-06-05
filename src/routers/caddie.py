# from fastapi import APIRouter, HTTPException
# from src.models.schemas import ShotInput
# from src.services.rec_club import rec_club_average_distance as calculate_club_recommendation


# router = APIRouter(
#     prefix="/caddie",
#     tags=["Golf Club Recs"]
# )

# @router.get("/rec_avg")
# def recommendation_club_average_distance(rangefinder_distance: int):
#     try:
#         recommended_club = calculate_club_recommendation(rangefinder_distance)

#         return {
#             "rangefinder_distance": rangefinder_distance,
#             "recommended_club": recommended_club,
#             "message": f"You should use a {recommended_club} for your {rangefinder_distance} yard shot!"
#             }

#     except TypeError as error:
#         raise HTTPException(
#              status_code=400,
#              detail=str(error)
#         )

#     except ValueError as error:
#         raise HTTPException(
#             status_code=400,
#             detail=str(error)
#         )
    
#     except LookupError as error:
#         raise HTTPException(
#             status_code=404,
#             detail=str(error)
#         )    
    
#     except Exception as error:
#             raise HTTPException(
#                 status_code=500, 
#                 detail="Something went wrong internally on our servers. We are looking into it!"
#             )
