# -*- coding: utf-8 -*-
"""
Created on August 14, 2024
Author: Blaine
Description: This is my practice codes for function.
"""


def greet_user(username):
    """显示问候语"""
    print(f"Hello, {username.title()}!")


greet_user('jesse')


def display_message():
    print("learning function.")


display_message()


def favorite_book(book_name):
    print(f"One of my favorite books is {book_name.title()}")


favorite_book('alice in wonderland')


# 传递实参  位置实参
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
describe_pet('dog', 'bubble')


# 关键字实参
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(animal_type='hamster', pet_name='harry')


# 参数默认值  使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('willie')


# practice 1
def make_shirt(size, slogan='I love python'):
    print(f"\nHere is you {size} T-shirt and your slogan is {slogan}!")


make_shirt('small')
make_shirt("medium", "gogogo")
make_shirt(slogan="fight", size='large size')


def describe_city(city, country='USA'):
    print(f"\n{city.title()} is in {country}.")


describe_city("China", "beijing")
describe_city(city='washington', country='USA')
describe_city(city='London', country='UK')


# 函数的返回值
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee')
print(musician)


# 返回字典
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 27)
print(musician)


# 函数结合while
# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     print("(Enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# practice
# def city_country(city, country):
#     city_info = f"\"{city}, {country}\""
#     return city_info
#
#
# while True:
#     print("\nPlease tell me your city info.")
#     print("(Enter 'q' at any time to quit)")
#     city = input("City: ")
#     if city == 'q':
#         break
#     country = input('Country: ')
#     if country == 'q':
#         break
#     print("------------------------------------------------")
#     # print(city_country('santiago', 'Chile'))
#     city_infos = city_country(city, country)
#     print(city_infos)
#     print("------------------------------------------------")

# practice make_album()

# def make_album(singer_name, song_name=None):
#     album_info = f"{singer_name} {song_name}"
#     return album_info
#
#
# while True:
#     print("\nEnter your favorite song and singer.")
#     print("Enter 'q' at any time to quit.")
#     singer_name = input("Singer name: ")
#     if singer_name == 'q':
#         break
#     song_name = input("Song name: ")
#     if song_name == 'q':
#         break
#
#     print(make_album(singer_name.title(), song_name.title()))

# 传递列表
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 在函数中修改列表
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# practice
# 编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages的列表中。
# 调用函数send_message()，再将两个列表都打印出来，确认正确移动了消息
def send_messages(messages, sent_messages):
    """
    打印每条消息并将其移动到 sent_messages 列表中。
    """
    while messages:
        current_message = messages.pop(0)  # 从 messages 列表中取出第一条消息
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)  # 将消息添加到 sent_messages 列表中


# 定义消息列表
messages = ["Hello!", "How are you?", "Goodbye!"]

# 定义一个空列表，用于存储已发送的消息
sent_messages = []

# 调用函数 send_messages()
send_messages(messages, sent_messages)

# 打印两个列表，确认消息是否已正确移动
print("\nFinal lists:")
print("Messages:", messages)  # 应该是空的，因为所有消息都已发送
print("Sent Messages:", sent_messages)  # 应该包含所有已发送的消息
