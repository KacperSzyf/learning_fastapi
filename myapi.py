#imports
from fastapi import FastAPI


#Main
app = FastAPI()

#Data
students = {
    1: {
        "name": "jane",
        "age": 20,
        "class": 2022
    }
}

#Endpoints
@app.get("/")
def index():
    return{"name": "test data"}
