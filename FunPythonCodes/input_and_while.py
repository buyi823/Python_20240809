# -*- coding: utf-8 -*-
"""
Created on August 13, 2024
Author: Blaine
Description: This is my practice codes for user input and while loops.
"""

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# name = input("Please enter you name: ")
# print(f"\nHello, {name}")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}")

# age = input("How old are you?")

# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# 求模运算
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# practice 1 汽车租赁
# rent = input("Let me see if I can find you a: ")
# print(rent)

# practice 2 restaurant oder
# order = input("How many people are you having dinner with: ")
# order = int(order)
# if order > 8:
#     print("Sorry we have no enough seats.")
# else:
#     print("All right, still have seats")

# practice 3 判断一个数是否是10的整数倍
# number = input("Please enter an arbitrary number and I can tell if it is a multiple of 10： ")
# number = int(number)
# if number % 10 == 0:
#     print("The number you entered is divisible by 10.")
# else:
#     print("The number you entered is not divisible by 10.")

# While loops
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# break statement
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")

# continue statement
current_number = 0;
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# practice 1

# while True:
#     pizza_topping = input("Please enter your pizza toppings: ")
#     if pizza_topping == "quit":
#         break
#     else:
#         print(f"\nOK, we'll add {pizza_topping} into you pizza.")

# practice 2
# while True:
#     age = input("Please enter your age: ")
#     print("Enter '0' to quit.")
#     age = int(age)
#     if age == 0:
#         break
#     elif age < 0:
#         print("Age cannot be negative.")
#     elif age < 3:
#         print("free")
#     elif 3 <= age < 12:
#         print("ten dollars")
#     else:
#         print("15 dollars")
#

# endless loop
# a = 2
# while True:
#     a *= a
#     print(a)

# 使用while循环处理列表和字典
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verified user: {current_users.title()}")
    confirmed_users.append(current_users)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除为特定值的所有元素列表
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response  # 将回答存储在字典中
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n--- Poll Result ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}")

# practice sandwich
# sandwich_orders = ['cheese', 'ham', 'vegetable', 'chicken', 'beef', 'tuna']
# finished_sandwiches = []
#
# while sandwich_orders:
#     cooking_sandwiches = sandwich_orders.pop()
#     print(f"I made your {cooking_sandwiches} sandwich.")
#     finished_sandwiches.append(cooking_sandwiches)
#
# for finished_sandwich in finished_sandwiches:
#     print(f"Here is your sandwiches: {finished_sandwich}")

sandwich_orders = ['pastrami', 'ham', 'vegetable', 'pastrami', 'pastrami', 'tuna']
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print("Sorry the pastrami sold out.")

# practice
responses = {}
polling_active = True
print("\nIf you could visit one place in the world, where would you go?")
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would you go? ")
    responses[name] = response  # 将回答存储在字典中
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to go {response}")

