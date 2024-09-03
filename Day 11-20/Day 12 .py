# Scope - were you write the variable defines its space
'''
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Inside the function : {enemies}")

increase_enemies()
print(f"Outside the funcion : {enemies}")
'''
# Namespace - give name to anything that has scope

# Block space concept not in python -- Block space  // Block - if, for , while loop  in python if variable 
# is decalared in a block then it can be accessed outside the block too

# Local Scope
'''
def drink_protion():
    potion_strength = 2
    print(potion_strength)
drink_protion()
'''

#  Global Scope
'''
player_health = 10

def drink_protion():
    potion_strength = 2
    print(player_health)
drink_protion()
'''

#  Modifying Global Scope
'''
enemies = 1

def increase_enemies():
    global enemies    # delcaring the global funciton is used below
    enemies += 2
    print(f"Inside the function : {enemies}")
    return enemies + 1       #insted of modifying the global variable

increase_enemies()
print(f"Outside the funcion : {enemies}")
'''

# Global scope really useful when declaring global constants
# Global Constants
'''
pi = 3.14159
URL = "https://www.goole.com"
Twitten_handle = "@fuck"
'''

# Guess the number Project 

import random

from random import randint

number = random.randint(0,100)
# number = randint(0,100)


live = 10
print('''Welcome to the number Guessing Game
I'm thinking of a number between 1 and 100''')


def game():
    global live

    level = input("Choose a difficulty : Type level Easy or Hard : ").lower()
    if level == 'hard' :
        live = 5
    
    def decide(user__input):
        """Checks answers against guess"""
        global number 
        if user__input > number :
            print("Too High ")
        else :
            print("Too Low" )
        
    while live > 0 :
        print(f"You have {live} attempts remaining to guess the correct answer")
        user_input = int(input("Make a guess : "))
        if user_input == number :
            print(f"You got it! The answer was {number}")
            break
        elif live > 0 :
            decide(user_input)
            live -=1
        if live >= 1:
            print("Guess Again")
    print("You've run out of guesss, you lose.")

game()