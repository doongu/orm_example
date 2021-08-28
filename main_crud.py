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
Base.metadata.create_all(engine)

# 테이블 생성 부분
demo = Demo(name="hello", math="world", english="new")
session.add(demo)

# update
# upt = session.query(Demo).filter(Demo.name =="hello").update({"name":"update this content"})
# print(upt)

# delete
# de = session.query(Demo).filter(Demo.name == "update this content").delete()
# print(de)
# print(session.query(Demo).count())

# read
# find_demos = session.query(Demo).filter_by(name="update this content").all()

# for each in find_demos:
#     print("select_result : ", each.name)


# coomit
session.commit()

