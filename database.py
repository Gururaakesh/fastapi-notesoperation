from sqlalchemy import Integer,Float,String,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

dataurl="postgresql+psycopg://postgres:root%40123@localhost:5432/gurudb"
Base=declarative_base()
engine=create_engine(dataurl)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)


class Product(Base):
    __tablename__="Notes"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    content=Column(String)