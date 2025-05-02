from fastapi import APIRouter
from models.enrollments_models import get_courses_id,get_students_id,enrolled_students
from pydantic import BaseModel
from fastapi.responses import JSONResponse
enrollment_router=APIRouter()

class enrollments(BaseModel):
    cousrse_id:str
    student_id:str

@enrollment_router.post("/enrolled_students")
async def enrolled():
    result=await enrolled_students()
    if not result:
        return JSONResponse(status_code=500,content={"message":"error adding students"})



@enrollment_router.post("/students/{students_id}")
async def get_student(student_id:int):
    result= await get_students_id(student_id)
    if not result:
        return JSONResponse(status_code=500,content={"message":"error adding students"})
    return JSONResponse(status_code=200,content={"message":result})

@enrollment_router.post("/courses/{courses_id}")
async def get_courses(courses_id:int):
    result=await get_courses_id(courses_id)
    if not result:
        return JSONResponse(status_code=500,content={"message":"error adding course"})
    return JSONResponse(status_code=200,content={"message":result})
