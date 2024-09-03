# numbers = [1,2,3,4]

# new_list = [n*2 for n in numbers]

# print(new_list)

# name = "Anuj"

# letter_list = [letter for letter in name]
# print(letter_list)

# range_list = [i*2 for i in range(1,5)]
# range_list_condition = [i*2 for i in range(1,5) if i%2==0]

# print(range_list)
# print(range_list_condition)

# names = ["Anuj", "Majnu", "Sachin", "Manish", "Himanshu"]

# upper_case_list = [name.upper() for name in names if len(name)>5 ]

# print(upper_case_list)


# --------------------------square number
'''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number*number for number in numbers]

print(squared_numbers)
'''
#------------- odd numbers

'''list_of_strings = input().split(',')

list_of_number = [int(num) for num in list_of_strings]

result = [num for num in list_of_number if num%2 ==0]

print(result)'''

# Common in file
with open("./file1.txt") as file:
    data1 = file.readlines()

with open("./file2.txt") as file:
    data2 = file.readlines()

# data1 = [int(item.strip()) for item in data1]
# data2 = [int(item.strip()) for item in data2]

common_data = [int(num) for num in data1 if num in data2]

print(common_data)