from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import VARCHAR
import pymysql
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test_orm', echo=True)

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

session_maker = sessionmaker(bind=engine)
session = session_maker()

Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Demo(Base):
    __tablename__ = 'new_test_table'
    
    name = Column(VARCHAR(45), primary_key=True)
    math = Column(VARCHAR(45))
    english = Column(VARCHAR(45))

Base.metadata.tables
# for k,v in Base.metadata.tables.items():
#     print(f"{k}: {v}")
Base.metadata.create_all(engine)

demo = Demo(name="hello", math="world", english="new")
session.add(demo)
# # find_demos = session.query(Demo).filter_by(name="hello").all()

# # for demo in find_demos:
# #     print(demo.name)

session.commit()