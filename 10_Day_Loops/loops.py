#!/usr/bin/python3

for i in range(0,11):
    print(i)
print()
count = 0
while count < 11:
    print(count)
    count = count + 1
print()
for i in range(1, 8):
    print(i * "#")
print()
for i in range(1, 9):
    print("#" * 8)
print()
for i in range(11):
    print(f"{i} x {i} = {i * i}")
print()
language = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in language:
    print(i)
add = 0
for i in range(0, 101):
    add = add + i
print(add)
add_even_num = 0
for i in range(0, 101, 2):
    add_even_num = add_even_num + i
print(add_even_num)

fruits = ["banana", "orange", "mango", "lemon"]

for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])
