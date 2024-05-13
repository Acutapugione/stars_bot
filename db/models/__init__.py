from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...


from .student import Student