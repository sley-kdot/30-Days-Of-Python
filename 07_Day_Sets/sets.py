#!/usr/bin/python3

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Dell", "HP", "Lenovo"])
print(it_companies)
it_companies.pop()
print(it_companies)

joined_sets = A.union(B)
print(joined_sets)
A.intersection(B)
print(A)
print(A.issubset(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

ages = set(age)
print(type(ages))

