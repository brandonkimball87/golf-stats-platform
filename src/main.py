from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models.schemas import ShotInput
from src.database.crud import create_shot, recommend_shot

app = FastAPI(
    title="Smart Caddie API",
    description="Tracking my golf shots to learn club distances",
    version="1.0.0",
    docs_url="/caddie", # Customize the URL path if you want
    redoc_url="/manual"    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    """A simple greeting route to verify the server is live."""
    return {"status": "Online", "message": "Welcome to your Smart Caddie backend!"}



@app.post("/shots")
def log_shot(shot: ShotInput):
    sucess = create_shot(shot)

    if not sucess:
        raise HTTPException(
            status_code=500,
            detail='Failed to save shot'
        )
    
    return {
        "status": "Success",
        "message": f"Successfully logged your {shot.club} shot to the database!"
    }


@app.get("/caddie/recommendation")
def get_club_recommendation(rangefinder_distance: int):
    recommended_clubs = recommend_shot(rangefinder_distance)

    if not recommended_clubs:
        return {
            "distance_requested": rangefinder_distance,
            "recommendations": [],
            "message": "No club history found within 10 yards of this distance yet. Go hit some shots!"
        }
    
    return {
        "distance_requested": rangefinder_distance,
        "recommendations": recommended_clubs,
        "message": f"Found {len(recommended_clubs)} clubs you normally hit around this distance."
    }