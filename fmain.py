from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import (
    insert_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_students
)

app = FastAPI()

#Student model
class Student(BaseModel):
    name : str
    age : int


# POST - Add a student
@app.post("/students")
def add_student(student : Student):
    return insert_student(student)


# GET - Get all students
@app.get("/students")
def get_students():
    return get_all_students()


# GET - Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id : int):
    student = get_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail = "Student not found")
    return student


# PUT - Update student details
@app.put("/students/{student_id}")
def update_student_details(student_id : int, student : Student):
    result = update_student(student_id, student)
    if not result:
        raise HTTPException(status_code=404, detail = "Student not found")
    return {"message" : "Student update successfully"}


# DELETE - Delete student by ID
@app.delete("/students/{student_id}")
def remove_student(student_id : int):
    result = delete_students(student_id)  
    if not result:
        raise HTTPException(status_code=404, detail = "Student not found")
    return {"message" : "Student deleted successfully"}