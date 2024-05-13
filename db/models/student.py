from typing import Any
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
)
from . import Base


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str]
    stars_count: Mapped[int]

    def __init__(self, name:str, stars_count:int):
        self.name = name
        self.stars_count = stars_count