"""print(len('Hello'))
print('Hello'[4])
a =9
b =8
print(a+b) 

123_234_34 # treated as 12323434 for readablilty python has this
"""
'''num_char = (len(input("What is your name ")))

print(type(num_char)) # check the type of variable

# Type casting

new_num_char = str(num_char)
print("Your name has "+new_num_char + " characters.")
'''

'''a =str(123) # float
print(type(a))'''

# Program
''''''
'''
num = (input("Enter a Two digit number "))
print(type(num))
num1 = num[0]
num2 = num[1]
print(int(num1) + int(num2))

print(2**2)  # power
'''
'''
# BMI Calculator




height = float(input("Enter the height in m : "))
weight = float(input("Enter the weight in kg : "))

BMI = int(weight/(height**2))
print("Your BMI is "+ str(BMI))

# round
print(round(2/8))
print(round(2/8 ,2))   # round up upto 2 digits
# Floor division
num = 2/3
print(type(2//3))
num /= 2


# User scores a point
score = 10 
score +=1

print(score)
'''
'''
#  F strings
a =3
b= 30 
c= 4
# F string // in front of string type f ,, ex f"Anuj"
print(f"a score is {a} , b score is {b} and c score is {c} ")
'''

#  Your Life in weeks
'''
age = int(input("What is your age ? "))
max_age = 90 ;

months = (age*12) ; #   age =max_age -90;
days = age * 365;
weeks = age *52;

M_months = (max_age*12) -months;
M_days = max_age * 365 -days;
M_weeks = max_age *52 - weeks;

# Also
# ans = f"You have {M_days} days, {M_weeks} weeks and {M_months} months left."

print(f"You have {M_days} days, {M_weeks} weeks and {M_months} months left.")
'''
#########Tip Calculator

bill = float(input("What is total bill ?\n"))
tip = int(input("What percent tip would you like to give ? 10, 12, or 15 ?\n"))
people = int(input("How many people to split the bill ? \n"))

pay1 = (bill/100*tip) + bill
print(pay1)
pay = round(pay1/people ,2)
pay = "{:.2f}".format(pay) # will round off 2 digit will add 0 in the end
print(f"Each guy will pay ${pay}")