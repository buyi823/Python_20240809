# -*- coding: utf-8 -*-
"""
Created on August 24, 2024,
Author: Blaine
Description: practice reconstruction
"""

import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is you name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n)")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")


greet_user()


# practice input your favorite number

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Enter your favorite number: ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
else:
    print(f"I know your favorite number! It's {number}")

