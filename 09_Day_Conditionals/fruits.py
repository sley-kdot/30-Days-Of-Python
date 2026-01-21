#!/usr/bin/python3

fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter your favorite fruit: ")
user_fruit.islower()
if user_fruit in fruits:
     print(fruits)
else:
    fruits.append(user_fruit)
    print(fruits)
