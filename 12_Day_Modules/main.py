#!/usr/bin/python3

import random
import string

def random_user_id():
    length = 6
    characters = string.ascii_lowercase + string.digits
    print(characters)

    random_str = ""
    for _ in range(length):
        random_chars = random.choice(characters)
        random_str = random_str + random_chars
    return random_str

print(random_user_id())

def user_id_gen_by_user():
    num_of_chars = int(input("Enter the number of charaters: "))
    num_of_id = int(input("Enter the number of IDs: "))

    characters = string.ascii_lowercase + string.digits

    random_str = ""
    for i in range(num_of_id):
        for j in range(num_of_chars):
            random_chars = random.choice(characters)
            random_str = random_str + random_chars
        random_str += "\n"
    return random_str
print(user_id_gen_by_user())

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f"rbg({red},{green},{blue})"

print(rgb_color_gen())

def list_of_hex_colors():
    character = string.ascii_lowercase
    alphanum = character[0:6] + string.digits
    
    hexa_list = []
    
    for i in range(5):
        random_str = "#"
        for j in range(6):
            random_chars = random.choice(alphanum)
            random_str += random_chars
        hexa_list.append(random_str)
    return hexa_list
print(list_of_hex_colors())

def list_of_rgb_colors():
    rgb_list = []
    for i in range(6):
        rgb_list.append(rgb_color_gen())
    return rgb_list
print(list_of_rgb_colors())

def generate_colors(color_type, number):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    character = string.ascii_lowercase
    alphanum = character[0:6] + string.digits

    result = []
    
    if color_type == "rgb":
        for i in range(number):
            result.append(f"rgb({red},{green},{blue})")
    elif color_type == "hexa":
        for i in range(number):
            random_str = "#"
            for j in range(6):
                random_chars = random.choice(alphanum)
                random_str += random_chars
            result.append(random_str)
    return result

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))
