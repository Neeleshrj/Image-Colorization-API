from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from colorizer import image_colorizer
from mega import Mega

app = FastAPI()

mega = Mega()
m = mega.login()

m.download_url('https://mega.nz/file/EMl2FAqR#f54U3M3-s7eMz-YAnsGvzqp1NsJkJme74UT0Tf9_Haw',"./model/")

class UserIn(BaseModel):
    imgObject: str

@app.get("/")
async def test_if_working():
    return "HELLO WORLD"

@app.post("/colorized", response_model=UserIn)
def colorized_image(user: UserIn):
    return image_colorizer(user.imgObject)