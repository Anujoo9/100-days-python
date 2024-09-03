# Functions with output
'''
def format_name(first_name ,last_name):
    # title function to convert into title ,,ex Hello My Name Is Anuj
    ans = first_name.title() +" "+ last_name.title()
    return f"{ans}"

ans =format_name("AnUJ" , "yADav")
print(ans)
'''
# Multiple return function
'''
def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = f_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name ? ") ,
      input("What is your last name ? ")))

'''

# Leap year modification
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False


def days_in_month(year, month):
    if month > 12 and month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]:


year = int(input("Enter a year :"))
month = int(input("Enter a month :"))
days = days_in_month(year, month)
print(days)
'''

# Docstrings // use it in the function it will be shown when we click on the function"""   """
# Also use it as multiline comment // python developers avoid multiline comment
'''
def format_name(f_name, l_name):
    """Take first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name =="":
        return "You didn't provide valid inputs"  # return as an ealry exit
    formated_f_name = f_name.title()
    formated_l_name = f_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

format_name()
'''
# Calculator

from logo import calculator
print(calculator)

# Add


def add(a, b):
    return a+b

# Subtract


def subtract(a, b):
    return a-b

# Multiply


def multiply(a, b):
    return a*b

# Divide


def divide(a, b):
    return a/b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    num1 = float(input("What is the First number ? "))

    for symbol in operations:
        print(symbol)

    flag = True

    while(flag == True):
        
        operation_symbol = input("Pick an operation from the line above : ")
        num2 = float(input("What is the next number ? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation : ") == 'y':
            num1 = answer
        else :
            flag = False
            calculator()

calculator()

