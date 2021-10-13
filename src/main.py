from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

from example import add

app = FastAPI()

class UserIn(BaseModel):
    imgname: str
    imgObject: str

@app.get("/")
async def read_root():
    return add(10,20)

@app.post("/colorized", response_model=UserIn)
def colorized_image(user: UserIn):
    return user

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}