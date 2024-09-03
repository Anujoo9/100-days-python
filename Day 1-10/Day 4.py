'''# Random Number Generator
import random

random_integer = random.randint(1,10)
print(random_integer)
# import my_module
# print(my_module.pi)

random_float = random.random() #random float
# random_float = random.random()*5 #random float increased rnge of random number
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

'''
# Head Tail
'''
import random
toss = random.randint(0,1)

if toss == 1:
    print("Head")
else:
    print("Tail")

'''
# List// order
'''
states_of_america = ["a","b","c","h","j"]
states_of_america[2] = "$"

print(states_of_america[0])
print(states_of_america)
'''
# Pay the bill // Random Guy will pay the bill//using split funciton
'''
import random
guys = ['Anuj','Prateek','Vidushi','Sristi']
guy = random.choice(guys)
print(guy)
'''
'''
import random
name_string = input("Give me names , seperated by a comma.\n")
names = name_string.split(",")
num_items = len(names) # gives length of list
random_choice = random.randint(0,num_items-1)
print(names[random_choice])
'''
'''
# List within a list
list1 = ['a', 'b','c','y']
list2 = ['d','e','u']

list3 = [list1,list2]
print(list3)
'''

'''
# Tresure Game
list1 = ['d','d','d']
list2= ['d','d','d']
list3 = ['d','d','d']
list = [list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
x = input("Enter coordinates")
h =int(x[0])-1
v =int(x[1])-1
list[h][v] = 'x'
print(f"{list1}\n{list2}\n{list3}")
'''

# Rock Paper Scissor 
import random

Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ='''  
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. To exit enter 00\n"))
    comp = random.randint(0,2)
    list =[Rock,Paper,Scissors]
    if choice == 0 and comp == 2: 
        print(f"Your choice \n {list[choice]} \nComp: \n {list[comp]}")
        print("You Win!!")
    elif choice == 1 and comp == 0:
        print(f"Your choice \n {list[choice]} \nComp: \n {list[comp]}")
        print("You win")
    elif choice ==2 and comp == 1:
        print(f"Your choice \n {list[choice]} \nComp: \n {list[comp]}")
        print("You win")
    elif comp == choice:
        print(f"Your choice \n {list[choice]} \nComp: \n {list[comp]}")
        print("Tie")
    elif choice >= 3:
        print("Wrong choice!")
    elif choice == 00:
        break
    else :
         print(f"Your choice \n {list[choice]} \nComp: \n {list[comp]}")
         print("You lose")
