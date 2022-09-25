#imports
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


#Main
app = FastAPI()

#Data
students = {
    1: {
        "name": "jane",
        "age": 20,
        "yearOf": 2022
    }
}

#Schema
class Student(BaseModel):
    name: str
    age: int
    yearOf: str

#Endpoints
@app.get("/")
def index():
    return{"name": "test data"}

#path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you would like to view:", gt = 0, lt = 3)):
    return students[student_id]

#query parameter
@app.get("/get-by-name/{student_id}")
def get_Student(student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Error": "Student not found!"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error" : "Student ID already Exists!"}

    students[student_id] = student
    return students[student_id]