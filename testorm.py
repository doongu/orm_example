
from sqlalchemy import create_engine

engine = create_engine('sqlite:///example.db', echo=True)

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

session_maker = sessionmaker(bind=engine)
session = session_maker()

Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Demo(Base):
    __tablename__ = 'demos'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


for k,v in Base.metadata.tables.items():
    print(f"{k}: {v}")

demo = Demo(name="hello", password="world")

find_demos = session.query(Demo).filter_by(name="hello").all()

for demo in find_demos:
    print(demo.name)

session.commit()