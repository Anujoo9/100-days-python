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
