'''#Rolllercoaster
print("Welcom to the rollercoaster!")
height = int (input("What is your height in cm ?"))

if height >= 120 :  # == !=
    print("You can ride the rollercoaster")
    age = int(input("What is you age ?"))
    if age <=12 :
      print("You can ride the rollercoaster! and Pay 5$")
    elif age <=18 :
      print("You can ride the rollercoaster! and Pay 7$")
    else :
        print("You can ride the rollercoster and pay 12$")

else:
    print("Sorry!, You have to grow taller before you can ride.")
'''

'''  
#   Odd even
num = int(input("Enter a number\n"))

if num%2 == 0:
    print("Number is Even")
else:
    print("Number is odd")
'''

# BMI Calculator
'''
height = float(input("Enter the height in m : "))
weight = float(input("Enter the weight in kg : "))

BMI = int(round(weight/(height**2,)))
print("Your BMI is "+ str(BMI))

if BMI < 18.5 :
    print(f"Underweight BMI is {BMI}")
elif  BMI < 25:
    print(f"Normal Weight BMI is {BMI}")
elif BMI < 30:
    print(f"Overweight BMI is {BMI}")
elif BMI < 35:
    print(f"Obese BMI is {BMI}")
else:
    print(f"Clinically obese BMI is {BMI}")
'''
#  Leap Year
'''
year = int(input("Enter a year"))

if year%4 == 0:
    if year%100 == 0:
        if year % 400 ==0:
             print("Leap Year")
        else:
            print("Not a Leap Year")
    else :
        print("Leap Year")
else:
    print("Not a Leap Year")

'''
# Roller Coaster
'''
print("Welcom to the rollercoaster!")
height = int (input("What is your height in cm ?"))
bill =0

if height >= 120 :  # == !=
    print("You can ride the rollercoaster")
    age = int(input("What is you age ?"))
    if age <=12 :
        bill =5
        print("Cild Tickets are 5$")
    elif age <=18 :
       bill =7  
       print("YOuth tickets are 7$")
    else :
        bill = 12
        print("Adult tickets are 12$")

    want_photo = input("Do you want photo ticket ? Y or N.")
    if want_photo == 'Y':
        bill +=3

    print(f"The final bill is {bill}")

else:
    print("Sorry!, You have to grow taller before you can ride.")

'''
# Pizza Order
'''
print("Welcome to Python Pizza Delivaries!")
size = input("What size pizza do you want ? S , M or L")
add_pepperoni  = input("Do you want pepperoni> Y or N")
extra_cheese = input("Do you want extra cheese ? Y or N")
bill = 0

if size == 'S':
    bill +=15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else :
    print("Wrong size")

if add_pepperoni == 'Y':
    if size == 'S':
        bill +=2
    else :
        bill +=3
if extra_cheese == 'Y':
    bill += 1

print(f"Your Final bill is ${bill}.")


'''
#  Logical Operators
# and or not 
'''
print("Welcom to the rollercoaster!")
height = int (input("What is your height in cm ?"))
bill =0

if height >= 120 :  # == !=
    print("You can ride the rollercoaster")
    age = int(input("What is you age ?"))
    if age <=12 :
        bill =5
        print("Cild Tickets are 5$")
    elif age <=18 :
       bill =7  
       print("YOuth tickets are 7$")
    elif age >= 45 and age <=  55:
            print("Enjoy, Everything is going to be OK Just enjoy :)")

    else :
        bill = 12
        print("Adult tickets are 12$")
        
    want_photo = input("Do you want photo ticket ? Y or N.")
    if want_photo == 'Y':
        bill +=3

    print(f"The final bill is {bill}")

else:
    print("Sorry!, You have to grow taller before you can ride.")

'''
# Love Calculator
'''
from tkinter import E


print("Welcome to the Love Calculator")
name1 = input("What is your name ? \n").lower()
name2 = input("What is their name ? \n").lower()
name = name1+name2

t = name.count('l')
r = name.count('o')
u = name.count('v')
e = name.count('e')
true = t+r+u+e
l= name.count('t')
o= name.count('r')
v= name.count('u')
e= name.count('e')

love = l+o+v+e

score = int(str(love) + str(true)) # becz look while countinng is reversed

if (score <=10) or (score >=90) :
    print(f'Your score is {score}, you go together like coke and mentos.')

elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}")


'''

# Final Project
Q1 = input("L or R\n").lower()
if Q1 == 'l':
    Q2 = input("swim or wait\n").lower()
    if Q2 == 'wait':
        Q3 = input("which door ? Red, Blue OR Yellow\n").lower()
        if Q3 == 'yellow':
                print("You Win")
        else:
            print("Game Over")
    else:
            print("Game Over")
else:
    print("Game Over")

'''

 o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                 "$
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$

'''
