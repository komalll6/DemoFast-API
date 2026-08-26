from fastapi import FastAPI

app=FastAPI()

#route
#path parameter- if we dont know the id

@app.get("/students/(student_id)") 
def get_studentbyid(student_id: int):
    return{
        "student details":  "student_id"
    }


#query parameter- pass query 
#EXAMPLE-  /students?crouse=python