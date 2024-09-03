# Balck Jack Project 

from hashlib import blake2b
import random
def deal_card():
    '''Retruns a Random card form the deck'''
    cards = [11 ,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def play_game():
    user_card = []
    computer_card = []

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())  # to add single item use append ,, use extend if you want to add list to it

    def calculate_sum(cards):
        """Take a list of cards and return the sum of the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if sum(cards) > 21 and 11 in cards :
            cards.remove(11)
            cards.append(1)
        
        return sum(cards) # sum function  ,, sum(iterable,/,start = 0)   # parammeters are not defined above so by default it uses as decribed

    is_game_over = False

    while is_game_over != True:
        user_score =calculate_sum(user_card)
        computer_score = calculate_sum(computer_card)

        print(f"    Your card:{user_card} , current score is : {user_score}")
        print(f"    Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card , type 'n' to get pass: ")
            if user_should_deal =='y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calculate_sum(computer_card)

    def compare(user_score , computer_score):
        if user_score == computer_score:
            return f"Draw :)"
        elif computer_score == 0:
            return "Lost , opponent has Blackjack"
        elif user_score == 0 :
            return "Win with a Blackjack"
        elif user_score > 21:
            return "You went over. You lose"
        elif computer_score < user_score:
            return "You win"
        else:
            return "You Lose"

    print(f"Your final hand:  {user_card} and score is  {user_score}")
    print(f"Computer's final hand:  {computer_card} and score is  {computer_score}")

    print(compare(user_score,computer_score))

import os
from logo import balackJack

while(True):
    print(balackJack)
    play_game()
    
    game = input("Do you want to play the BalckJack ? Type 'y' or 'n' ").lower()
    if game == 'n':
        break
    os.system('cls||clear')
    