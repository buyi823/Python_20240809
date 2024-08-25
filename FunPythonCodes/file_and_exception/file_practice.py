# -*- coding: utf-8 -*-
"""
Created on August 23, 2024,
Author: Blaine
Description: file practice
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)  # 该输出多了一个空行，read()到达文件末尾时，返回一个空字符串，显示出来就是一个空行
print(contents.rstrip())

# file_path = "C:\\Users\\Administrator\\Desktop\\introduce myself.txt"
# with open(file_path, 'r', encoding='utf-8') as file_object:
#     contents = file_object.read()
# print(contents)

# 逐行读取
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# 想在with代码块外访问文件内容可以将文件各行内容存储在一个列表中
# with open('pi_digits.txt') as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())

# with open('pi_digits.txt') as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(f"{pi_string[:10]}")
# print(len(pi_string))

# 圆周率包含你的生日吗
# with open('pi_million_digits.txt') as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# birthday = input("Please enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


# practice 1
file_name = 'D:\\Source Codes\\Python\\FunPythonCodes\\file_and_exception\\learning_python.txt'
# 读取整个文件
# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents)

# 遍历文件对象
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.strip())

# 将文件存储在列表中，并在with外打印
with open(file_name) as file_object:
    lines = file_object.readlines()

file_strings = ''
for line in lines:
    file_strings += line

print(file_strings)

# practice 2
# 将learning_python.txt中的每一行python替换成C
message = "I really like dogs."
print(message.replace('dog', 'cat'))

with open(file_name) as fn:
    contents = fn.read()
    print(f"before replace:\n{contents}")
    print(f"after replaced:\n{contents.replace('Python', 'C')}")
