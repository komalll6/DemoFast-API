from fastapi import FastAPI


app = FastAPI()

# @app.get("/queryparam")
# def get_query(name:str, age:int):
#     return{
#         "name":name,
#         "age":age
#     }

data=[    #in memory data
    {
    "id":1,
    "name":"koml",
    "age":22
},
{
    "id":2,
    "name":"dia",
    "age":15
}
]

@app.get("/getalldata")
def get_all():
        return data

@app.get("/getoneoutofall/{name}")
def get_one(name: str):
        for item in data:
                if item["name"] == name:
                        return item
        return {"data": "not found"}

@app.post("/adddata")
def add_data(student: Student):
        newData = {
                "id": len(data) + 1,
                **student.model_dump()
        }
        data.append(newData)
        return newData

# @app.get("/getalldata")
# def get_all():
#     return data

# @app.get("/getoneoutofall/{id}")
# def get_one(id:int):
#     for item in data


#http://127.0.0.1:8000/queryparam?name=komal
#http://127.0.0.1:8000/queryparam?name=komal&age=22 - if we give age:int