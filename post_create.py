from fastapi import FastAPI

from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int

app= FastAPI()

students = []

# @app.get("/queryparam")
# def get_query(name: str):
        
#         return {"name": name}

# @app.get("/students/{student_id}")
# def get_studentbyid(student_id: int):
#     return {"student details": student_id}

@app.post("/students")
def create_student(student: Student):
    new_student={
        "id":len(student)+1,
        **student.model_dump()
    }
    students.append(new_student)
    return new_student