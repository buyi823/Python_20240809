cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print(True)
else:
    print(False)

# 检查特定的值是否包含在列表中
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print(True)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age = 17
if age >= 18:
    print('You are old enough to vote!')
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
# 下面的写法更简洁
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print("\nFinished making you pizza!")

# 外星人颜色练习
alien_colors = ['green', 'yellow', 'red']
if 'green' in alien_colors:
    print("Your get 5 points.")
if 'yellow' in alien_colors:
    print("Your get 10 points.")
if 'red' in alien_colors:
    print("Your get 15 points.")

# 人生的不同阶段
age = 40
if age < 2:
    print("baby")
elif 2 < age < 4:
    print("kid")
elif 4 < age < 13:
    print("child")
elif 13 < age < 20:
    print("teenager")
elif 20 < age < 65:
    print("adult")
else:
    print('elder')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinish making your pizza.")

# practice
print("==================================")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# practice1
users = ['Dorthy', 'John', 'Michael', 'admin', 'kobe', 'james']
for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
users.clear()  # 清除列表元素，保留列表
print(users)
if not users:
    print("we need to find some users.")

# practice-2
current_users = ['Dorthy', 'John', 'Michael', 'admin', 'kobe', 'james']
new_users = ['james', 'kobe']
for new_user in new_users:
    if new_user in current_users:
        print(f"\"{new_user}\" The name has been taken. please input another name.")

# practice-3
# 假设有两个数组
array1 = ['Hello', 'world', 'PYTHON']
array2 = ['hello', 'WORLD', 'python']

# 将两个数组中的元素都转换为小写，然后进行比较
if [element.lower() for element in array1] == [element.lower() for element in array2]:
    print("两个数组的元素相同（不区分大小写）")
else:
    print("两个数组的元素不同（不区分大小写）")

# practice-4
ordinal_numeral = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in ordinal_numeral:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number == 4:
        print("4th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    else:
        print("9th")
