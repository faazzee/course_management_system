from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from models.courses_models import add
from fastapi import APIRouter

course_router=APIRouter()

class courses(BaseModel):
    title:str
    description:str

@course_router.post("/courses/")
async def add_courses(request:courses):
    session=await add(title=request.title,description=request.description)
    if not session:
        print("gg")
