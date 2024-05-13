from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from .models import (
    Base,
    Student
)


engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(bind=engine)

def up():
    Base.metadata.create_all(engine)


def down():
    Base.metadata.drop_all(engine)