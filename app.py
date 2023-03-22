from fastapi import Depends, FastAPI, HTTPException, Path
from pydantic import BaseModel

from database import engineconn
from models import Test

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()


class Item(BaseModel):
    name: str
    number: int


@app.get("/")
async def first_get():
    example = session.query(Test).all()
    return example
