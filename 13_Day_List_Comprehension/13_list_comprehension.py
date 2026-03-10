#!/usr/bin/python3

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

result = [num for num in numbers if num <= 0]
print(result)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_result = [col for row in list_of_lists for col in row]
print(list_result)
