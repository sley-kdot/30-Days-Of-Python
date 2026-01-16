#!/usr/bin/python3
import math

# Day 3: 30 Days of python programming

age = 28
height = 1.72
complex_num = (4 + 4j)

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base * height
print("The area of a Triangle is ", area_of_triangle)

a = int(input("Enter side a of the triangle: "))
b = int(input("Enter side b of the triangle: "))
c = int(input("Enter side c of the triangle: "))
perimeter_of_triangle = a + b + c
print("The perimeter of the triange is ", perimeter_of_triangle)

length = int(input("Enter the lenght of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
perimeter_of_rectangle = 2 * (length * width)
print("The perimeter of the rectangle is ", perimeter_of_rectangle)

radius = int(input("Enter the radius of a circle: "))
PI = 3.14
area_of_circle = PI * radius ** 2
circum_of_circle = 2 * PI * radius
print("The area of a circle: ", area_of_circle)
print("The circumference of a circle: ", circum_of_circle)

x1, x2 = 2, 2
y1, y2 = 6, 10
#slope = ((10 - 6) / (2 - 2))
distance = math.sqrt(((2 - 2) **2) + ((10 - 6) **2))
#print("the slope is :", slope)
print("the distance is :", distance)

python_length = len("python")
dragon_length = len("dragon")
print(python_length > dragon_length)

if "on" in "python" and "dragon":
    print(True)

if "on" not in "python" and "dragon":
    print(True)

sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print(True)

print(float(python_length))
print(str(python_length))

num = int(input("enter an even num: "))
if (num % 2) == 0:
    print(True)

floor_num = 7 // 3
print(floor_num == int(2.7))

print("10" == 10)
print(int("9.8") == 10)
