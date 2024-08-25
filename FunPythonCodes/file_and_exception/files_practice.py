# -*- coding: utf-8 -*-
"""
Created on August 24, 2024,
Author: Blaine
Description: exception practice
"""

# 用户输入两个数，判断是否是数字，两个数字相加
# print("Enter 'q' at any time to quit.")
# print("Please enter two numbers.")
#
# while True:
#     try:
#         x = input("Give me a number: ")
#         if x == 'q':
#             break
#         x = int(x)
#
#         y = input("Give me another number: ")
#         if y == 'q':
#             break
#         y = int(y)
#
#     except ValueError:
#         print("Please enter a number.")
#
#     else:
#         sum_numbers = x + y
#         print(f"{x} + {y} = {sum_numbers}")

# 猫和狗的文件， 读取这些文件，文件不在时提示FileNotFound

# filenames = ['dogs.txt', 'cats.txt']
#
# for filename in filenames:
#     print(f"Reading file: {filename}")
#
#     try:
#         with open(filename) as f:
#             contents = f.read()
#             print(contents)
#
#     except FileNotFoundError:
#         print("The file cannot be found.")


# 计算某个单词出现了多少次
line = "Row, row, row your boat"
print(f"'row' appear: {line.count('row')}")
print(f"'row' appear: {line.lower().count('row')}")
print(line)


def count_common_words(filename, word):
    """计算指定的单词在图书中出现了多少次"""
    # 请注意，这里计算得到的结果并不准确，比实际出现的次数要多。
    try:
        with open(filename, encoding='utf-8') as f:
            book_contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = book_contents.lower().count(word)
        msg = f"{word} appears in {filename} about {word_count} times."
        print(msg)


filename = 'alice.txt'
count_common_words(filename, 'the')
