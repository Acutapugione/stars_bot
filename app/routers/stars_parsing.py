from aiogram import Router
from utils.stars_parser import parse_students_starts
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message
from db import Session, Student
from sqlalchemy import select
import logging
import json


router = Router(name="stars_parsing_router")

def get_students_data() -> dict[str:int]:
    with Session.begin() as session:
        students = session.scalars(select(Student)).all()
        students_data = { 
            student.name: student.stars_count 
            for student in students 
        }
        return students_data

def upsert_students_data(data: dict[str:int]) -> None:
    with Session.begin() as session:
        for student_name, stars_count in data.items():
            exsited_student = session.scalar(
                select(Student)
                .where(Student.name == student_name)
            ) 
            if exsited_student:
                exsited_student.stars_count += stars_count
                session.add(exsited_student)
            else:
                session.add(Student(
                    name = student_name,
                    stars_count = stars_count,
                ))
            

@router.message(F.text.contains("Відвідуваність:"))
@router.message(F.text.contains("Зірочки за заняття:"))
async def attendance_handler(message: Message) -> None:
    try:
        text = message.text
        students_stars = parse_students_starts(text, search_str="Відвідуваність:")
        students_stars.update(parse_students_starts(text, search_str="Зірочки за заняття:"))
        print(f"{students_stars=}")
        upsert_students_data(students_stars)
        await message.answer(f"Дані успішно оновлено!")
    except Exception as e:
        logging.error(str(e))
        await message.answer(f"Дані не було оновлено!")

@router.message(Command("students_stars"))
async def students_stars_handler(message: Message) -> None:
    students_data = get_students_data()
    # answer_text = json.dumps(students_data, ensure_ascii=False)
    answer_text = "\n".join(f"{key} => {val}" for key, val in students_data.items())
    await message.answer(answer_text)