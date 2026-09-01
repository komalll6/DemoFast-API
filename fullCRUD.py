#to remove - use delete method
#index mei apne ap remove krdega => enumerate
#mongodb atlas =>online cloud based ( fastapi + mongodb atlas) => CRUD operations
#mongodb are noSQL databases

#pip install pymongo => hv mongodb client(funcion give connection string)

from fastapi import FastAPI

from pydantic import BaseModel

app= FastAPI()

#temp storage
class Student(BaseModel):
    name:str
    age:int
    course:str

students = [
{
    "id": 1,
    "name": "Ram",
    "age": 20,
    "course": "python"
},
{
    "id": 2,
    "name": "Shyam",
    "age": 22,
    "course": "java"
},
{
    "id": 3,
    "name": "Rose",
    "age": 21,
    "course": "c++"
}
]


#get all students => GET METHOD
@app.get("/students")
def get_students():
    return students


#get method => get student by id
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"message": "Student not found"}


#create method => with post method
@app.post("/students")
def create_student(students: Student):
    new_student={
        "id":len(students)+1,
        **students.model_dump()
    }
    students.append(new_student)
    return new_student


#create update method => with put method
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student.update(updated_student.model_dump())
            return existing_student
        
    return{"message": "Student not found"}



#delete student by id => DELETE METHOD
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students): #needfor index => use enumerate => to get the index of the student in the list
        if student["id"] == student_id:
            students.pop(index) #pop = helps to remove the element from the list
            return {"message": "Student deleted successfully"}
    return {"message": "Student not found"}