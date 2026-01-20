#!/usr/bin/python3

dog = dict()
print(dog)

dog = {"name":"Akuke" , "color":"Brown" , "breed":"Local" , "legs":4 , "age":3}
print(dog)

student = {
        "first_name":"Silas",
        "last_name": "Auta",
        "gender": "Male",
        "marital_status": "Single",
        "skills":["Football", "Tennis"],
        "Country":"Nigeria",
        "City":"Kaduna",
        "Address":"Angola Crescent"
        }
print(len(student))
check_val = type(student.get("skills"))
print(check_val)
student["skills"].append("Singing")
print(student)
keys = student.keys()
print(keys)
values = student.values()
print(values)
print(student.items())
student.pop("City")
print(student)
del student["Address"]
print(student)

