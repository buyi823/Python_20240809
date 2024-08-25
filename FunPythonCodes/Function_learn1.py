"""
Created on August 19-20, 2024
Author: Blaine
Description: This is my practice codes for function.
"""


# 使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print(f"\nMaking a {size}-pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(12, 'pepperoni')
make_pizza(16, 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese')


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


# PRACTICE 1
def make_sandwich(*types):
    print("You sandwich: ")
    print(types)


make_sandwich("ham")
make_sandwich("vegetable", "ham", "beef")


# practice 2
def user_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


user = user_profile('Blaine', 'Xu', location='lingbao', field='nojob')
print(user)


# practice 3
def player_profile(first_name, last_name, **player_info):
    player_info['first_name'] = first_name
    player_info['last_name'] = last_name
    return player_info


player = player_profile('Kobe', 'Bryant', location='Los Angeles')
print(player)


# practice 4
def vehicle_profile(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car = vehicle_profile('Ford', 'F150', place_of_production='USA', vehicle_type='Pickup')
print(car)


