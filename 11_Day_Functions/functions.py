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

def capitalize_list_items(list_param):
    my_list = []
    for i in range(len(list_param)):
        word = list_param[i].capitalize()
        my_list.append(word)
    return my_list
print(capitalize_list_items(["david", "kingsley", "solomon"]))

def add_item(list_param, item):
    list_param.append(item)
    return list_param
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))

def remove_item(list_param, item):
    list_param.remove(item)
    return list_param
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

def sum_of_numbers(number):
    add_num = 0
    for i in range(1, number + 1):
        add_num = add_num + i
    return add_num
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def sum_of_odds(number):
    add_odd_num = 0
    for i in range(1, number + 1, 3):
        add_odd_num = add_odd_num + i
    return add_odd_num
print(sum_of_odds(5))
print(sum_of_odds(10)) 
print(sum_of_odds(100))

def sum_of_even(number):
    add_even_num = 0
    for i in range(1, number + 1, 2):
        add_even_num = add_even_num + i
    return add_even_num
print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(100))


