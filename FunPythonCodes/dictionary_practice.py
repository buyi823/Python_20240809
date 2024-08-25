# -*- coding: utf-8 -*-
"""
Created on August 12, 2024
Author: Blaine
Description: This is my practice codes for learning the dictionary.
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0  # 添加键值对
alien_0['y_position'] = 25
print(alien_0)
# 修改字典
alien_0['color'] = "red"
alien_0['speed'] = "medium"
alien_0['increment'] = "5"
print(alien_0)
# del key-value
del alien_0['increment']
print(alien_0)
# dictionary format
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# 使用get()方法
point_value = alien_0.get('points', 'test')
print(point_value)
point_value = alien_0.get('lalala', 'No lalala value assigned.')  # 没有指定Key的情况，可以输出自定义信息
print(point_value)

# practice-1
friend = {'first_name': 'Michael', 'last_name': 'Jordan', 'age': 34, 'city': 'Chicago'}
print(friend)

# practice-2
favorite_numbers = {'Kobe': 8, "Jordan": 23, 'james': 23, 'Duncan': 21, 'Iverson': 3}
print(f"Iverson favorite number is {favorite_numbers['Iverson']}")

# practice-3
print('practice-3')
program_terminology = {'method': 'blablabla', "function": '', "class": '', 'arguments': '', 'aaa': 'bbb'}
print(program_terminology)
for key, value in program_terminology.items():
    print(f"{key} is a {value}. ")

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
# items返回键值对列表 items()
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# 遍历字典中的key
print("遍历字典中的key")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for key in favorite_languages:
    print(key.title())
# keys()返回key   keys()方法实际返回的是一个列表
for key in favorite_languages.keys():
    print(key.title())
# 判断key是否在字典中
if 'jen' in favorite_languages.keys():
    print("jen good")
if 'erin' not in favorite_languages.keys():
    print("eric, please take out poll!")
# 按特定顺序遍历字典中的所有键 sorted()
print("按特定顺序遍历字典中的所有键")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# 默认是reverse=False对字典的键进行升序排序，可以省略
# 升序排列
print("升序")
for name in sorted(favorite_languages.keys(), reverse=True):
    print(f"{name.title()}, thank you for taking the poll.")

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# 如果字典中有大量重复的值，可以使用set()提取不重复的值
print("使用set()去除重复值")
for language in set(favorite_languages.values()):
    print(language.title())

# 以下是集合，没有键值对的情况是集合
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

# practice 1
rivers = {'nile': 'egypt', 'yangzi': 'china', 'Mississippi': 'USA'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

# practice 2
print("practice2")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
users = ['jen', 'phil']
for user in favorite_languages:
    if user in users:
        print(f"Thank you {user}!")
    if user not in users:
        print(f"You wanna join in {user.title()}?")

# 嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
print(aliens)
for alien in aliens:
    print(alien)

# 生成30个键值对
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# print(aliens)
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:10]:
    print(alien)
print("...")

# 在字典中存储列表
print("在字典中存储列表")
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'], }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# 字典的嵌套
print("字典的嵌套")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# practice 1
print("practice 1------------------")
pets = {"john": 'bubble', 'kobe': 'harry', 'michael': 'dot'}
print(pets)
for owner, pet in pets.items():
    print(f"Hi, I'm {owner.title()}. This is my pet {pet.title()}.")

# practice 2
print("practice 2 字典中存储列表")
favorite_places = {
    'kobe': ['roma', 'los angels', 'philadelphia'],
    'Michael': ['chicago', 'new york', 'Wilmington'],
}
for name, places in favorite_places.items():
    print(f"I'm {name.title()}.")
    print("My favorite places are:")
    for place in favorite_places:
        print(place.title())

# practice 3
print("practice 3 city")
cities = {
    "London": {'country': 'UK', 'population': '10000000', 'fact': 'There is a big ben in London.'},
    "New York": {'country': 'USA', 'population': '12000000', 'fact': 'The nickname is Big Apple.'},
    "Paris": {'country': 'France', 'population': '10000000', 'fact': 'city of romantic.'},
}
for city, infos in cities.items():
    print(f"\nThis is {city}. ")
    for key, value in infos.items():
        print(f"{key}: {value}")