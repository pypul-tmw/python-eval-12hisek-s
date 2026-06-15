import json

student = [
{
    "id": 1,
    "name":"Abhishek",
    "course":"Python",
    "marks":90
},

{
    "id": 2,
    "name":"Ash",
    "course":"C",
    "marks":90
}
]
with open("student.json","w") as file:
    json.dump(student,file, indent = 4)

print("JSON file created successfully")