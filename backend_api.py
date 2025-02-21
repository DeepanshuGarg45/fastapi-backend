from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    data: Optional[List[str]] = []

# Constants for user details
USER_ID = "Deepanshu45"
EMAIL = "deepanshugarg.2455@gmail.com"
ROLL_NUMBER = "22BAI71427"

@app.post("/bfhl")
async def process_data(request: RequestData):
    # Validate input
    if not request.data:
        raise HTTPException(status_code=400, detail="Invalid request. 'data' field is required.")

    # Separate numbers and alphabets
    numbers = [item for item in request.data if item.isdigit()]
    alphabets = [item for item in request.data if item.isalpha()]
    
    # Get the highest alphabet (case insensitive)
    highest_alphabet = max(alphabets, key=lambda x: x.upper(), default=None)
    highest_alphabet = [highest_alphabet] if highest_alphabet else []

    # Response structure
    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

    return response

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}
