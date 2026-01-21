#!/usr/bin/python3

person={ 
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
            }
        }

if "skills" in person:
    mid_skill = person.get("skills")
    print(mid_skill[2])
if "skills" in person:
    if "Python" in person.get("skills"):
        skill_list = person.get("skills")
        get_skill_idx = person.get("skills").index("Python")
        print(skill_list[get_skill_idx])
if person.get("is_married") == True and person.get("country") == "Finland":
    first_name = person.get("first_name")
    last_name = person.get("last_name")
    country = person.get("country")
    print(f"{first_name} {last_name} lives in {country}. He is married")

