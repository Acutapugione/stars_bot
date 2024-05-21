def parse_students_starts(data:str, search_str:str = "Зірочки:\n", star_char:str ='⭐️')->dict[str:int]:
    student_stars = {}
    section_index = data.find(search_str)
    
    section = data.strip()[section_index:]
    rows = section.split('\n')[1:]
    for row in rows:
        if star_char in row.strip():
            print(row.split("-"))
            student, stars_string, *_ = row.split("-")
            student_stars[student.strip()] = stars_string.count(star_char)
    return student_stars