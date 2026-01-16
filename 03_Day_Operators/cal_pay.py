#!/usr/bin/python3

# a script that prompts the user to enter hours and rate per hour. Calculate pay of the person

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
product = hours * rate
print("Your weekly earning is ", product)
