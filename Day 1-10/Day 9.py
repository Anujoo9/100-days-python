# Dictionaries in Python //Syntax = {key:value}
'''
programming_dicitionary = {
"Bug": "An error in a program that prevents the program from running as expected.",
"Funciton": "A piece of code that yu can easliy call over and over again.",
"Loop":"The action of doing someting over and over again.",
123 :"Heloo"
}
# Retriving item from dicitionary

print(programming_dicitionary['Bug'])
print(programming_dicitionary[123])

# Adding data
programming_dicitionary["wow"] = "Wowweeeee"
print(programming_dicitionary)

# Empty dictionar

empty_dictionary = {}
empty_dictionary['item'] = 'sfd'
'''

'''/n#  Wipe an existing dictionary'''
'''
# programming_dicitionary = {}
# print(programming_dicitionary)

# Edit an item in a dictionary
programming_dicitionary["Bug"] = "A moth in your computer"  # if key not there then it will create or if exists then edited

for i in programming_dicitionary: 
    print(i)# only get keys
    print(programming_dicitionary[i]) # value line by line
'''
# Grading Program
'''
student_scores = {
    "Anuj":99,
    "Harry": 74,
    "Himanshu":89,
    "Abhay" : 78,
    "Ayush" : 77,
    "Kunal":0
}

student_grade ={}

for score in student_scores:
    if  91 < student_scores[score] <= 100: 
        student_grade[score] = "Outstanding"
    elif 81 < student_scores[score] <= 90:
        student_grade[score] = "Exceeds Expections"
    elif 71 < student_scores[score] <=80:
        student_grade[score] = "Acceptable"
    else:
        student_grade[score] = "Fail"

print(student_grade)

'''

#  Nesting Dicitionary
'''
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
#  Nesting a List in a Dicitionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in Dicitionary

city_visited = {
    "France": {"Paris": "Food", "Lille": "Fun"},
    "Germany": {"Berlin": "fun", "Hamburg": "Beach"}
}
travel_log = {
    "France": {"city_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"city_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 7}
}
# Nesting a Dicitonary in a List

travel_log = [
    {"country": "France",
    "city_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12, },
    {"country": "Germany", 
    "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 7}
]
'''
# Dicitonary in a List Excercise
'''
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(nation , visits , cities):
    # new_country = {
    # "country" : nation
    # ,"visit" : visits , 
    # "city": cities}
    # travel_log.append(new_country)
    # Or 
    new_country = {}
    new_country["country"] = nation
    new_country["visit"] = visits
    new_country["city"] = cities
    travel_log.append(new_country)

add_new_country("Russia" , 2 , ["Moscow" , "Saint Petersbeg"])

print(travel_log)

print(travel_log)

'''

# Secreat auction program
from logo import Hammer
import os 
print(Hammer)
bids = {}
flag = True
while flag:
    def add_bid():
        
        name = input("Enter your name: ")
        money = int(input("What is you bid ?:  $"))
        bids[name] = money
        os.system('cls')
    
    add_bid()
    exit = input("Are there any other bidder. Types 'Yes' or 'no'").lower()
    if exit == 'no':
        flag = False

max = 0
max_key = ''
for bidder in bids:
   if max < bids[bidder]:
        max_key = bidder

print(f"The bid goes to {max_key} and the bid is ${bids[max_key]}")

 







































