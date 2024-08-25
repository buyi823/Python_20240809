# -*- coding: utf-8 -*-
"""
Created on August 20, 2024
Author: Blaine
Description: This is my practice codes for class.
"""


# 创建和使用类

class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Harry', '1')
your_dog = Dog('Bubble', 3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old.")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} year old.")
your_dog.sit()
your_dog.roll_over()


# practice 1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a good restaurant_name.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now and it is a {self.cuisine_type}.")


some_restaurant = Restaurant('Dumplings_Restaurant', 'Chinese restaurant')
print(some_restaurant)
some_restaurant.describe_restaurant()
some_restaurant.open_restaurant()


# practice 2
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a nice person.")

    def greet_user(self):
        print(f"Hi {self.first_name} {self.last_name}!")


user_info = User('Michael', 'Jordan')
user_info.describe_user()
user_info.greet_user()
