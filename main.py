from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from colorizer import image_colorizer

app = FastAPI()

class UserIn(BaseModel):
    imgObject: str

@app.get("/")
async def test_if_working():
    return "HELLO WORLD"

@app.post("/colorized", response_model=UserIn)
def colorized_image(user: UserIn):
    return image_colorizer(user.imgObject)