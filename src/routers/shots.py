from fastapi import APIRouter, HTTPException
from src.models.schemas import ShotInput
from src.database.crud import create_shot


router = APIRouter(
    prefix="/shot_data",
    tags=["Shot Data"]
)

@router.post("/upload")
def upload_shot(shot: ShotInput):
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