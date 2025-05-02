from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

Base=declarative_base()
engine=create_engine('sqlite:///students.db',echo=False)


async def create_db():
    Session=sessionmaker(bind=engine)
    session=Session()
    return session
