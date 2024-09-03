'''
def greet():
  pass
   

greet()

def greet_with_name(name):
    print(f''Hello {name}.
          How are you')

greet_with_name('Anuj')
'''

# Positional Arguments
'''
def greet_with(name,location):
  print(f"Hello {name}")
  print(f"Your location is {location}")

greet_with('Anuj', 'Hell')
'''
# Key word arguments
'''
def func(a=1,b=4,c=4):
  pass
'''
'''
def greet_with(name,location):
  print(f"Hello {name}")
  print(f"Your location is {location}")

greet_with(name = "anuj",location = 'fun')
greet_with(location = "anuj",name = 'fun')
'''

# Q. Need paint to paint the wall
'''
import math
def no_of_cans(height, width , coverage):
  cans = math.ceil(((height*width) / coverage))
  print(f"Number of required cans is {cans}")

height = int(input("Enter the height of the wall: "))
width = int(input("Enter the width of wall: "))
coverage = 5

no_of_cans(height,width, coverage)
'''

#  Prime number checker
'''
number = int(input("Enter a number : "))
def Prime(number):
  flag = False
  for i in range(2,number):
    if number % i*i == 0:
      flag = True
  
    elif i*i > number:
      break
      
  if flag == False:
    print(f"The {number} is prime number")
  
  else:
    print(f"The {number} is not prime number")
    
'''
# --------------------------------------------------------------------------------------
# Caesar Cipher
'''

import turtle
from logo import logo
from turtle import position

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(plain_text , shift_amount , ceaser_direction):
    end_text = ""
    if ceaser_direction == 'decode':
            shift_amount *=-1
    for letter in plain_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          new_position = position + shift_amount
          if new_position>25:
            new_position = shift%25
          elif new_position < 0:
           new_position = 25%shift                      # insted of using % copy letter again so index will be more than 25
          new_letter = alphabet[new_position]
          end_text += new_letter
        else:
          end_text += letter
    print(f"The {direction}d text is {end_text}")
    
should_continue = True
while should_continue:
  try:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
      text = input("Type your message: \n").lower()
      shift = int(input("Type the shift number: \n"))
      shift %= 26
  except:
      print("Wrong input")

  ceaser(plain_text = text , shift_amount=shift, ceaser_direction= direction)
  exit = input("Types 'Yes' if you want to go again. Otherwise type 'no'.\n")
  if exit == 'Yes':
    should_continue = False
    print("Good Bye...")
        '''
# ------------------Long method


# def encrypt(plain_text ,shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
    # if new_position>25:
    #     new_position = shift%25
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The encoded text is {cipher_text}")

# def decode(plain_text ,shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     if new_position < 0:
#         new_position = 25%shift
#     new_letter = alphabet[new_position]
#     cipher_text += new_letter
#   print(f"The decoded text is {cipher_text}")


# if direction == 'encode':
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction == 'decode':
#     decode(plain_text = text, shift_amount = shift)


# ------------------
# from turtle import position

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabet.index('c'))