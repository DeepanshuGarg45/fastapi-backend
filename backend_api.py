from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

class RequestData(BaseModel):
    data: List[str]

USER_ID = "Deepanshu45"
EMAIL = "deepanshugarg.2455@gmail.com"
ROLL_NUMBER = "22BAI71427"

@app.post("/bfhl")
async def process_data(request: RequestData):
    numbers = [item for item in request.data if item.isdigit()]
    alphabets = [item for item in request.data if item.isalpha()]
    highest_alphabet = max(alphabets, key=lambda x: x.upper(), default=None)
    highest_alphabet = [highest_alphabet] if highest_alphabet else []
    
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
