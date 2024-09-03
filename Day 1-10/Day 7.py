# HANGMAN
# My Code
'''Teacher Code'''
# step 1
# import random 
# word_list = ["ardvark", "baboon", "camel"]
# a = random.choice(word_list)
# print(a)
# chance = 10
# guess = 0
# s = ''

# while chance > 0:
#     x = input("Guess a letter\n").lower()
#     if x in a:
#         s +=x
#         guess +=1
#         chance -=1
#     elif guess == len(a) -1:
#         break
#     else:
#         chance -=1
# print(s)

# Step 1
'''
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
'''

# Step 2

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")
    
display =[]
for i in chosen_word:   #for i in range(len(chosen_word))
    display += '_'

print(display)
    
print(f'Pssst, the Solution is {chosen_word}.')
