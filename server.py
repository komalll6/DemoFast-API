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

#fastapi - to run
#unicorn 