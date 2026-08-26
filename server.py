from fastapi import FastAPI

app = FastAPI() #app obj is used to create

#route

@app.get("/home")    # @ = decorator, .dot are used in fastapi, get- method, /- path
def home():
    return{
        "message": "Welcome to FastApi"
    }

@app.get("/aboutUs")
def aboutUs():
    return{
        "message": "Here this is about page"
    }

@app.get("/student")
def student():
    return{
        "message": "Hey! I'm the student of MCA-3 SEM"
    } 



#fastapi - to run
#unicorn 