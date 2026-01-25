#!/usr/bin/python3

def add_two_numbers(num1, num2):
    add = num1 + num2
    return add
print(add_two_numbers(4, 4))

def area_of_circle(radius):
    PI = 3.14
    return PI * radius * radius
radius = int(input("Enter the radius: "))
print(area_of_circle(radius))

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit
print(convert_celsius_to_fahrenheit(50))

def check_season(month):
    spring = ["march", "april", "may"]
    summer = ["june", "july", "august"]
    autumn = ["september", "october", "november"]
    winter = ["december", "january", "february"]

    if month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    elif month in autumn:
        return "Autumn"
    else:
        return "Winter"
print(check_season("september"))

def solve_quadratic_eqn():
    pass

def print_list(list_param):
    for i in range(len(list_param)):
        print(list_param[i])
my_list = ["KDB", "Benardo", "Haaland", "Cherki"]
print_list(my_list)

def reverse_list(array):
    my_list = []
    for i in range(len(array) - 1, -1, -1):
        my_list.append(array[i])
    return my_list
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
