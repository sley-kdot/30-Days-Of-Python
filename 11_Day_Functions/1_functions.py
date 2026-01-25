#!/usr/bin/python3

def evens_and_odds(number):
    count_even = 0
    count_odd = 0
    for i in range(int(number) + 1):
        if i % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
    return f"The number of odds are {count_odd}.\nThe number of evens are {count_even}"
print(evens_and_odds(100))

def is_empty(param):
    if param:
        return "It's not empty"
    else:
        return "It is empty"
my_list = []
print(is_empty(my_list))

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()
greet("Nnamdi")
def show_args(**args):
    for key, val in args.items():
        print(f"{key}: {val}")
show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")
