from sqlalchemy import insert,delete,Column,String,Integer,select
from database.sqlite_connections import create_db,engine
from sqlalchemy.orm import declarative_base

Base=declarative_base()
class students(Base):
    __tablename__='STUDENTS'

    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)

    def __repr__(self):
        return f"<student(id={self.id},name='{self.name}',email='{self.email}')>"

Base.metadata.create_all(engine)

async def add_students(name,email):
    try:
        session=await create_db()
        query=insert(students).values(name=name,email=email)
        session.execute(query)
        session.commit()
        return True
    except Exception as e:
        print(f"error recieved as {e}")
        import traceback
        traceback.print_exc()
    finally:
        session.close()