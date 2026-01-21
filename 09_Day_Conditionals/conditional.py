#!/usr/bin/python3

user = int(input("Enter your age: "))

if user >= 18:
    print("You are old enough to drive")
else:
    print(f"You need {18 - user} more years to learn to drive")

my_age = 25
your_age = int(input("Enter your age: "))

if my_age > your_age:
    print(f"You are {my_age - your_age} year(s) younger than me")
elif my_age < your_age:
    print(f"You are {your_age - my_age} year(s) older than me")
else:
    print("We are age mate")

first_num = int(input("Enter number one: "))
second_num = int(input("Enter number two: "))

if first_num > second_num:
    print(f"{first_num} is greater than {second_num}")
elif first_num < second_num:
    print(f"{first_num} is less than {second_num}")
else:
    print(f"{first_num} is equal to {second_num}")

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("You scored an A")
elif score >= 80 and score <= 89:
    print("You scored a B")
elif score >= 70 and score <= 79:
    print("You scored a C")
elif score >= 60 and score <= 69:
    print("You scored a D")
else:
    print("You scored an F")

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]

month = input("Enter your month: ").capitalize()

if month in autumn:
    print("The season is Autumn")
elif month in winter:
    print("The season is Winter")
else:
    print("The season is Spring")

