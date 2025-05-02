from fastapi import APIRouter
from models.enrollments_models import get_courses_id,get_students_id
from pydantic import BaseModel
enrollment_router=APIRouter()

class students(BaseModel):
    name:str
    email:str

@enrollment_router.post("/students/{students_id}")
async def get_student(student_id:int):
    result= await get_students_id(student_id)
    if not result:
        print("gg")

@enrollment_router.post("/courses/{courses_id}")
async def get_courses(courses_id:int):
    result=await get_courses_id(courses_id)
    if not result:
        print("gg")