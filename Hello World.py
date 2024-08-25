from decimal import Decimal

print("Hello World")
# 变量的使用 20240810
name = "ada lovelace"
print(name)
# upper()  lower()   title()
print(name.upper())
print(name.lower())
print(name.title())

# f"{variable}{variable}"
first_name = "ada"
middle_name = "m"
last_name = "lovelace"
full_name = f"{first_name} {middle_name} {last_name}"
print(f"Hello,{full_name.title()}")
full_name = "{} {}".format(first_name,last_name) # python 3.6以前的版本用这种方法
print(full_name)

# \n \t
print("Language:\nPython\nC\nJavaScript")
print("Language:\nPython\n\tC\n\tJavaScript")

# rstrip() lstrip()
favorite_language = 'python '
print(favorite_language.rstrip())
favorite_language = '  python'
print(favorite_language.lstrip())

# 引号
message = "One of Python's strengths is its diverse community"
print(message)
message1 = 'One of Python\'s strengths is its diverse community'
print(message1)

# practice
scientist_first_name = "albert"
scientist_last_name = "einstein"
scientist_aphorism = "\"A person who never made a mistake never tried anything new.\""
famous_name = f"{scientist_first_name.title() } {scientist_last_name.title() }"
print(famous_name + " once said, " + scientist_aphorism)

# 数据处理
"""
计算机在处理浮点数时，使用的是二进制表示法。某些十进制小数在二进制中无法精确表示，只能用近似值表示。举个例子：

0.1 在二进制中是一个无限循环的数：0.00011001100110011001100110011001100110011001100110011...
0.2 在二进制中也是一个无限循环的数：0.00110011001100110011001100110011001100110011001100110...
因为这些数在二进制中不能被精确表示，计算机内部存储的其实是它们的近似值。当你将它们相加时，近似值的误差会累积，从而导致最终结果也不完全精确。

在 Python 中，0.1 + 0.2 实际上接近 0.3，但由于浮点数表示的误差，它的精确值会稍微大一点，变成 0.30000000000000004。
"""
a = 0.1
b = 0.2
print(a+b)
print(round(a+b, 1)) # round

# from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(result)  # 输出 0.3

# 数中的下划线
universe_age = 14_000_000_000
print(universe_age)

# 同时给多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)
my_favorite_number = 8
tips = "My favorite number is: "
print(tips + str(my_favorite_number))  # 不同的变量类型连接转换一下
print(tips, my_favorite_number)   # 不同的变量类型可以逗号分隔直接输出
print(f"{tips}{my_favorite_number}")  # 格式化变量的方式
print("{}{}".format(tips, my_favorite_number))   # 这样也可以
print("%s%d" % (tips, my_favorite_number))  # %的方式