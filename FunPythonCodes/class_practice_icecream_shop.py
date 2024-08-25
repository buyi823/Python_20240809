# -*- coding: utf-8 -*-
"""
Created on August 20, 2024,
Author: Blaine
Description:
编写一个名为IceCreamStand的类，继承9-1的Restaurant类，添加一个名为flavors的属性，用于存储一个由各种口味的
冰激淋组成的列表。编写一个显示这些冰激凌的方法，创建一个IceCreamStand实例，并调用这个方法。
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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(f"The available ice cream flavors are: ")
        for flavor in self.flavors:
            print(f"- {flavor}")



# 创建 IceCreamStand 的实例
ice_cream_stand = IceCreamStand("Sweet Treats", "Desserts", ["Vanilla", "Chocolate", "Strawberry", "Mint"])

# 调用描述餐馆的方法
ice_cream_stand.describe_restaurant()

# 调用显示冰激凌口味的方法
ice_cream_stand.show_flavors()
