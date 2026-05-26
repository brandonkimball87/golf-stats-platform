from fastapi import FastAPI, HTTPException
from src.models.schemas import ShotInput
from src.database.crud import create_shot

app = FastAPI(title="Smart Caddie API")

@app.get("/")
def read_root():
    """A simple greeting route to verify the server is live."""
    return {"message": "Welcome to your Smart Caddie backend!"}


@app.post("/shots")
def log_shot(shot: ShotInput):
    """
    The Web Gatekeeper route. It catches incoming user data,
    hands it over to crud.py to save, and reports the results.
    """
    # Pass the validated data object to our database engine
    success = create_shot(shot)
    
    # If crud.py returns False (meaning the database hit an error)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to save shot to database")
        
    # If everything went perfectly, return a success response
    return {"status": "Success", "message": "Shot logged perfectly!"}