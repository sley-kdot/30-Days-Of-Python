#!/usr/bin/python3

my_list = list()
fruits = ["Orange", "Apple", "Watermelon", "Pineapple", "Grapes"]
print(fruits[0])
print(fruits[2])
print(fruits[4])

mixed_data_type = ["Nnamdi", "28", "1.72", "Single", "Kaduna"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(mixed_data_type)
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
it_companies[4] = "Tesla"
print(it_companies)
it_companies.append("Dell")
print(it_companies)
it_companies.insert(4, "Instagram")
print(it_companies)
it_companies.extend("#")
print(it_companies)
does_exist = "Tesla" in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
it_companies.pop(0)
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
full_stack = front_end
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
add = ages[0] + ages[9]
print(add)
median = ages[4] + ages[5] / 2
print(median)
average = sum(ages) / len(ages)
print(average)
range_val = ages[9] - ages[0]
print(range_val)
