from fastapi import APIRouter, HTTPException
from src.models.schemas import ShotInput
from src.database.db_setup import DatabaseManager
from src.database.shot_queries import ShotService

router = APIRouter(
    prefix="/shot_data",
    tags=["Shot Data"]
)


@router.post("/upload")
def upload_shot(shot: ShotInput):
    s = ShotService()
    sucess = s.upload_shot_to_db(shot_data = shot, table = table)

    if not sucess:
        raise HTTPException(
            status_code=500,
            detail='Failed to save shot'
        )
    
    return {
        "status": "Success",
        "message": f"Successfully logged your {shot.club} shot to your {table} table!"
    }

