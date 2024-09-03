# This program takes name and then randomly selects one person
# Who is going to pay the bill


import random
guys = input("Give me names , seperated by a comma.\n")
guy = guys.split(",")
noo = random.choice(guy)
print(f"{noo} is going to pay the bill.")