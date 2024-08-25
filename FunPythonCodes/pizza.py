"""
Created on August 20, 2024
Author: Blaine
Description: This is my practice codes for function.
"""

# 将函数存储在模块中
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")