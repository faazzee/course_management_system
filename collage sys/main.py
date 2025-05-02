from fastapi import FastAPI
from controllers.courses_router import course_router
from controllers.enrollments_router import enrollment_router
from controllers.students_router import student_router

app=FastAPI()
app.include_router(course_router,prefix='/api',tags=['users'])
app.include_router(enrollment_router,prefix='/api',tags=['users'])
app.include_router(student_router,prefix='/api',tags=['users'])