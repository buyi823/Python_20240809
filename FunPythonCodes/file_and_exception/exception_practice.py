# -*- coding: utf-8 -*-
"""
Created on August 23, 2024,
Author: Blaine
Description: exception practice
"""

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# 文件异常


# 分析文本
title = "Alice in Wonderland"
print(title.split())
print(title.split())

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")
# else:
#     words = contents.split() # 将所有从文件读出的单词以空格分开赋值给words
#     num_words = len(words)   # 计算所有单词的个数
#     num_characters = 0
#     for word in words:
#         num_characters += len(word)  # 每个单词的个数循环加起来就是字数
#     print(f"The file {filename} has about {num_words} words and {num_characters} characters.")


# 假设有一个列表，其中包含字符串
my_list = ["apple", "banana", "cherry"]

# 计算列表中所有字符串的字符总数
# total_chars = sum(len(item) for item in my_list)
# 以下的写法也行
total_chars = 0
for item in my_list:
    print(len(item))
    total_chars += len(item)

print(f"列表中总字符数为: {total_chars}")


# 使用多个文件
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# 静默， 有异常的情况保持静默
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # pass 起到一个占位符的作用，如果不写with语句，可以后续可以添加代码
        pass
        with open('missing_files.txt', 'a') as f:
            f.write('FileNotFoundError')
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
