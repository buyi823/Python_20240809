# -*- coding: utf-8 -*-
"""
Created on August 22, 2024,
Author: Blaine
Description: A collection of classes
"""


from datetime import datetime


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


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['can add post', 'can delete post', 'can ban user']
            self.privileges = privileges

    # 定义显示权限的方法
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")