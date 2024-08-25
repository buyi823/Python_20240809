# -*- coding: utf-8 -*-
"""
Created on August 20, 2024,
Author: Blaine
Description: This is my practice codes for class and instance.
"""

from datetime import datetime


# 使用类和实例

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 5

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(25)
my_new_car.read_odometer()

print("------This is the dividing line------")

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# practice
print("\n-------------dividing line---------------")


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 20

    def describe_restaurant(self):
        print(f"{self.name} is a good restaurant_name.")

    def open_restaurant(self):
        print(f"{self.name} is open now and it is a {self.cuisine_type}.")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
            print(f"This restaurant has been served {self.number_served}")
        else:
            print("Wrong served number.")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"This restaurant increase {self.number_served}")


restaurant_info = Restaurant('KFC', 'Fast Food')
restaurant_info.describe_restaurant()
restaurant_info.open_restaurant()

restaurant_info.set_number_served(18)
restaurant_info.increment_number_served(0)


# practice 2

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_user(self):
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            print(f"Good morning, {self.first_name} {self.last_name}!")
        elif 12 <= current_hour < 18:
            print(f"Good afternoon, {self.first_name} {self.last_name}!")
        else:
            print(f"Good evening, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self, count):
        self.login_attempts += count
        print(f"You have already attempted it {self.login_attempts} times.")
        if self.login_attempts > 5:
            print("Sorry, you have tried too many times, please confirm your password.")

    def reset_login_attempts(self):
        self.login_attempts = 0


user_info = User('Blaine', 'Xu')
user_info.greet_user()
user_info.increment_login_attempts(2)
# user_info.increment_login_attempts(2)
# user_info.increment_login_attempts(1)
# user_info.increment_login_attempts(2)
user_info.reset_login_attempts()
user_info.increment_login_attempts(2)