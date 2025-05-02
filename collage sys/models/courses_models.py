from sqlalchemy import insert,delete,Column,Integer,String,select
from sqlalchemy.orm import declarative_base
from database.sqlite_connections import create_db,create_engine,engine

Base=declarative_base()

class courses(Base):
    __tablename__='courses'

    id=Column(Integer,primary_key=True)
    title=Column(String)
    description=Column(String)

    def __repr__(self):
        return f"<courses(id={self.id},title='{self.title}',description={self.description})"

Base.metadata.create_all(engine)
async def add(title,description):
    try:
        session=await create_db()
        query=insert(courses).values(title=title,description=description)
        session.execute(query)
        session.commit()
        return True
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("error recieved {e}")
    finally:
        session.close()

