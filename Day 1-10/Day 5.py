# Loops
# For loop
'''
fruits = ["Apple" , "Peach" , "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)

    '''
# AVerage sutent heights 
# students_height = [ 10 ,12 ,13 ,15]
'''
students_height = input("Input a list of students heights ").split()
avg =0 
len =0
for i in students_height:
    avg +=int(i)
    len += 1
print(round(avg/len))
'''
'''
# Highest Score
scores = input("Enter a list of scores\n").split()
# max = 0
for i in range(0,len(scores)):
    scores[i] = int(scores[i])
# for i in scores:
#     if max < int(i):
#         max = int(i)

# print(f"Max score is {max}")
# --OR
print(max(scores))# min

'''
'''
# For in range
sum = 0
# for i in range(0,101,3): # gap og 3
for i in range(1,101):
    sum+= i
print(sum)

'''    
'''
# Adding evens
sum = 0
for i in range(1,101):
    if i%2 ==0:
        sum+=i
print(sum)
# Other way
sum =0
for i in range(2,101 ,2):
        sum+=i
print(sum)
'''

# FizzBuzz
'''
for i in range(1,101):
    if i%3 ==0 and i % 5 ==0:
        print(f"FizzBuzz Number is {i}")
    elif i%3 ==0:
        print(f"Fizz Number is {i}")
    elif i%5 ==0:
        print(f"Buzz Number is {i}")

        '''
# Password Generator
'''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password ?\n"))
nr_symbols = int(input(f"How many symbols would you like ? \n"))
nr_number = int(input(f"How many numbers would you like ? \n"))
'''
# Easy Level
# hj12?)/ sequencial
'''
password = ""
for i in range(0,nr_letters):
    password += random.choice(letters)
for i in range(0,nr_number):
    password +=random.choice(numbers)
for i in range(0,nr_symbols):
    password +=random.choice(symbols)
print(password)
'''


# Hard Level // using list and suffling the list
# Random 1n.5J*
'''
passwordList = []
for i in range(0,nr_letters):
    passwordList.append(random.choice(letters))
for i in range(0,nr_number):
    passwordList.append(random.choice(numbers))
for i in range(0,nr_symbols):
    passwordList.append(random.choice(symbols))
print(passwordList)
random.shuffle(passwordList)
print(passwordList)

password = ''
for char in passwordList:
    password +=char

print(f"Your password is {password}")

'''
# a = [1,2,5,9]
# import random
# random.shuffle(a) # Shuffle for list only
# print(a) 