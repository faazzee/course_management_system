from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from models.courses_models import add
from fastapi import APIRouter
from fastapi.responses import JSONResponse
course_router=APIRouter()

class courses(BaseModel):
    title:str
    description:str

@course_router.post("/courses/")
async def add_courses(request:courses):
    session=await add(title=request.title,description=request.description)
    if not session:
       return JSONResponse(status_code=500,content={"message":"error adding students"})
    return JSONResponse(status_code=200,content={"message":"successful"})
