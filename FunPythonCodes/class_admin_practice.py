# -*- coding: utf-8 -*-
"""
Created on August 21, 2024,
Author: Blaine
Description:
编写一个名为Admin的类，让它继承User类。添加一个名为privileges的属性，用喻存储一个字符串（如“can add post"、
"can delete post"、"can ban user"等）组成的列表。编写一个名为show_privileges()的方法，显示管理员的权限。创建一个
Admin实例，并调用这个方法。
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


# admin_privileges = Admin('Blaine', 'Xu',
#                          ['can add post', 'can delete post', 'can ban user'])
admin_user = Admin('Blaine', 'Xu')

admin_user.greet_user()
admin_user.privileges.show_privileges()