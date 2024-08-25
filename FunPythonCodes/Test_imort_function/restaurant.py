# -*- coding: utf-8 -*-
"""
Created on August 22, 2024,
Author: Blaine
Description: Restaurant类
"""


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} is a good restaurant_name.")
        print(f"cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open.")