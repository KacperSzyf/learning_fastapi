#imports
from fastapi import FastAPI


#Main
app = FastAPI()

#Endpoints
@app.get("/")
def index():
    return{"name": "test data"}
