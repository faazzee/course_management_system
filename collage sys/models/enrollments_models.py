from sqlalchemy import insert,select,delete,Column,String,Integer
from sqlalchemy.orm import declarative_base
from database.sqlite_connections import create_db
from models.courses_models import courses
from models.students_models import students
Base=declarative_base()

class Enrollments(Base):
    __tablename__='ENROLLMENT'
    id=Column(Integer,primary_key=True)
    student_id=Column(Integer)
    course_id=Column(Integer)


    def __repr__(self):
        f"<enrollment(id={self.id},student_id={self.student_id},course_id={self.course_id})>"

async def get_students_id(student_id:int):
    try:
        userlist=[]
        stmt=(select(Enrollments,students)
        .select_from(Enrollments)
        .join(students,students.id==Enrollments.student_id))
        session=await create_db()
        result=session.execute(stmt).scalars().all()
        for user in result:
            userlist.append({"id":user.id})
        return userlist
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"error getting the message{e}")
        return None
    finally:
        session.close()
async def get_courses_id(course_id:int):
    try:
        userlist=[]
        stmt=(select(Enrollments,courses)
        .select_from(Enrollments)
        .join(courses,courses.id==Enrollments.course_id))
        session=await create_db()
        result=session.execute(stmt).scalars().all()
        for user in result:
            userlist.append({"id":user.id})
        return userlist
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"error getting the message{e}")
        return None
    finally:
        session.close()
"so i need to get all the students details "