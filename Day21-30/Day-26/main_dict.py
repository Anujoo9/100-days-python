'''
import random
names = ["Anuj", "Rahul", "Himanshu", "Sristhi"]

students_score = {student:random.randint(1,100) for student in names}


print(students_score)

passed_students = {name:score for (name,score) in students_score.items() if score >= 33}

print(passed_students)
'''
# Exercie

# sentence = input()
# # sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# # sentence_list = sentence.split()

# result = {key:len(key) for key in sentence.split()}

# print(result)

# Excercise 2 temp conversion

# temp_c = {"Monday":12, "Tuesday": 14, "Wednesday": 15, "Thrusday": 17, "Friday": 18, "Saturday": 17, "Sunday":14}
# temp_c = eval(input())

# temp_f = {day:int((temp*9/5) +32) for (day,temp) in temp_c.items()}

# print(temp_f) 

# pandas
import pandas
student_dict = {
    "student": ["Anuj", "Himanhsu","Ran"],
    "score": [2,3,4]

}

student_data_frame =pandas.DataFrame(student_dict)
print(student_data_frame)
#
# Loop Through a data frame
# for (key,value) in student_data_frame.items():
#     print(key)

# Loop through rows of a datafram
for(index, row) in student_data_frame.iterrows():
    print(row.student)