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

#delete student by id => DELETE METHOD
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students): #needfor index => use enumerate => to get the index of the student in the list
        if student["id"] == student_id:
            students.pop(index) #pop = helps to remove the element from the list
            return {"message": "Student deleted successfully"}
    return {"message": "Student not found"}


#put => to update the student details