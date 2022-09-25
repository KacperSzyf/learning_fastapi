#imports
from fastapi import FastAPI, Path


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

#path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you would like to view:", gt = 0, lt = 3)):
    return students[student_id]

#query parameter
@app.get("/get-by-name")
def get_Student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return ("Error": "Student not found!")
