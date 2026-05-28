
# from src.models.schemas import ShotInput
# from src.database.crud import create_shot, recommend_shot, shot_history
# from src.services.rec_club import rec_club_average_distance


# @app.get("/caddie/recommendation")
# def get_club_recommendation(rangefinder_distance: int):
#     recommended_clubs = recommend_shot(rangefinder_distance)

#     if not recommended_clubs:
#         return {
#             "distance_requested": rangefinder_distance,
#             "recommendations": [],
#             "message": "No club history found within 10 yards of this distance yet. Go hit some shots!"
#         }
    
#     return {
#         "distance_requested": rangefinder_distance,
#         "recommendations": recommended_clubs,
#         "message": f"Found {len(recommended_clubs)} clubs you normally hit around this distance."
#     }







from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import caddie, shots 

app = FastAPI(
    title="Smart Caddie API",
    description="Tracking my golf shots to learn club distances",
    version="1.0.0",
    docs_url="/19birdies",
    redoc_url="/manual"    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(caddie.router)
app.include_router(shots.router)

@app.get("/")
def read_root():
    return {"status": "Online"}