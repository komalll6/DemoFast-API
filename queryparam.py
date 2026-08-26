from fastapi import FastAPI

app = FastAPI()

@app.get("/queryparam")
def get_query(name:str, age:int):
    return{
        "name":name,
        "age":age
    }


#http://127.0.0.1:8000/queryparam?name=koma
#http://127.0.0.1:8000/queryparam?name=komal&age=22 - if we give age:int