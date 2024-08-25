# -*- coding: utf-8 -*-
"""
Created on August 23, 2024,
Author: Blaine
Description: file practice
"""

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 添加文件而不是覆盖，可以以附加模式打开文件，如果文件不存在则新建

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# practice 1
# guest_name = 'guest_name.txt'
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# with open(guest_name, 'w') as file_object:
#     file_object.write(first_name)
#     file_object.write(last_name)

# practice 2  用户输入名字，将名字存入文件
# guest_book = 'guest_book.txt'
# print("Enter 'quit' when you are finished.")
# while True:
#     name = input("Please enter your name: ")
#     if name == 'quit':
#         break
#     else:
#         with open(guest_book, 'a') as file_object:
#             file_object.write(f"{name}\n")
#         print(f"Hi {name}, you've been added to the guest book.")


# practice 询问用户为何喜欢编程，当用户输入原因后，将其添加到文件中
# questionnaire_survey = 'D:\\Source Codes\\Python\\FunPythonCodes\\file_and_exception\\questionnaire_survey.txt'
# print("Enter 'quit' when you are finished.")
# while True:
#     reason = input("Why do you like programming?\n")
#     if reason == 'quit':
#         break
#     else:
#         with open(questionnaire_survey, 'a') as file_object:
#             file_object.write(f"{reason}\n")


# 上面练习的官方答案
file_name = 'D:\\Source Codes\\Python\\FunPythonCodes\\file_and_exception\\programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming?")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n)")
    if continue_poll != 'y':
        break
    with open(file_name, 'a') as f:
        for response in responses:
            f.write(f"{response}\n")

