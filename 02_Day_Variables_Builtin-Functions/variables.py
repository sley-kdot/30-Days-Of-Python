#!/usr/bin/python3
import math

# Day 2: 30 Days of python programming

first_name = "Nnamdi"
last_name = "Okonmah"
full_name = "Nnamdi Kingsley Okonmah"
country = "Nigeria"
city = "Kaduna"
age = 28
year = 2026
is_married = False
is_true = True
is_light_on = True
middle_name, language, nickname = "Kingsley", "Igbo", "KDot"

# Check the data type of all variables using type() built-in function
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(middle_name)
type(language)
type(nickname)

print(len(first_name))
print(len(last_name))
num_one, num_two = 5, 4
total = num_one + num_two
print("sum of 5 and 4 is: ", total)
subtract = num_one - num_two
print("minus 4 from 5: ", subtract)
mult = num_one * num_two
print("product of 5 and 4: ", mult)
div = num_one / num_two
print("divide: ", div)
mod_div = num_two % num_one
print("remainder of 4 / 5: ", mod_div)
exponent = num_one ** num_two
print("exponent is: ", exponent)
floor_div = num_one // num_two
print("floor division: ", floor_div)

radius = 30
area_of_circle = (math.pi * (radius ** 2))
print("The area of a circle is: ", area_of_circle)

circum_of_circle = (2 * math.pi) * radius
print("The circumference of a circle: ", circum_of_circle)

user_radius = int(input("Enter a radius: "))
area = math.pi * (user_radius ** 2)
print("AREA OF A CIRCLE: ", area)

first_name = input("Enter your first name: ")
print(first_name)
last_name = input("Enter your last name: ")
print(last_name)
country = input("Enter your country: ")
print(country)
age = input("Enter your age: ")
print(age)

