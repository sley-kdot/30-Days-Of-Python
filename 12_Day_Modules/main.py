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
