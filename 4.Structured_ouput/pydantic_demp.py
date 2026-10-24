from pydantic import BaseModel

class Student(BaseModel):
    name : str
    
new_student = {'name':'Sarthak'}

student = Student(**new_student)

print(type(student))