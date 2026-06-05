from fastapi import APIRouter, HTTPException
from src.models.schemas import ShotInput
from src.database.shot_queries import ShotService

router = APIRouter(
    prefix="/shot_data",
    tags=["Shot Data"]
)


@router.get("/users")
def get_unique_users_in_db(table_name: str):
    s = ShotService()
    user_list = s.get_unique_users(table_name = table_name)
    
    if user_list is not None and not user_list.empty:
        users = user_list.iloc[:, 0].tolist()
        return users

    raise HTTPException(
            status_code=404,
            detail='No users found'
        )


@router.post("/upload")
def upload_shot(shot: ShotInput, table_name: str = 'shots'):
    s = ShotService()
    sucess = s.upload_shot_to_db(shot_data = shot, table_name = table_name)

    if not sucess:
        raise HTTPException(
            status_code=500,
            detail='Failed to save shot'
        )
    
    return {
        "status": "Success",
        "message": f"Successfully logged your {shot.club} shot to your {table_name} table!"
    }

