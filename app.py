from fastapi import FastAPI, Path

from typing import Optional

from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"hari",
        "age":28,
        "address":"siphal"
    },
    2:{
        "name":"shyam",
        "age":21,
        "address":"Basundhara"
    },
    3:{
        "name":"geeta",
        "age":34,
        "address":"germany"
    }
}

@app.get("/")
def index():
    return {"name":"First Date"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]


'''
Let's discuss about the query parameter
'''

#google.com/results?search=Python
'''
The Optional in Optional[str] is not used by FastAPI, 
but will allow your editor to give you better support and detect errors.
'''
@app.get("/get-by-name")
def get_student(*,name: Optional[str] = None, test: int):
    #getting the student using the for loop
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data":"No Information Found"}


#Request body and the post method.

class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

#post method
@app.post("/create-student/{student_id}")
def create_student(student_id:int, student: Student):
    if student_id in students:
        return {"Error":"Student exists"}
    students[student_id] = student
    return students[student_id]


#put method
@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    students[student_id] = student
    return students[student_id]

@app.get("/students")
def get_all_students():
    return Student[students]


@app.delete('/student/{student_id}')
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    del students[student_id]
    return {"Message":"Student deleted successfully"}