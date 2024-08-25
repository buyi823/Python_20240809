# -*- coding: utf-8 -*-
"""
Created on August 22, 2024,
Author: Blaine
Description: Test the import of multiples classes
"""


from class_model import Admin, Privileges

user_info = Admin('Blaine', 'Xu')
user_info.greet_user()

user_access = Privileges()
user_access.show_privileges()
