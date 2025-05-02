from fastapi import APIRouter
from models.students_models import add_students
from pydantic import BaseModel
from fastapi.responses import JSONResponse
student_router=APIRouter()

class students(BaseModel):
    name:str
    email:str

@student_router.post("/students/")
async def add_student(request:students):
    result= await add_students(name=request.name,email=request.email)
    if not result:
       return JSONResponse(status_code=500,content={"message":"error adding students"})




