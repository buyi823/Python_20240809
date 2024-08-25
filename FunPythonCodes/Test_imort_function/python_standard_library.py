# -*- coding: utf-8 -*-
"""
Created on August 22, 2024,
Author: Blaine
Description: Study Python standard library
"""
import random
from random import randint, choice

print(randint(1, 6))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(choice(players))


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    # 定义 roll_die 方法，生成 1 到 sides 之间的随机数
    def roll_die(self):
        return randint(1, self.sides)


# 创建一个 6 面的骰子实例
six_sided_die = Die()
for _ in range(10):
    print(six_sided_die.roll_die())

ten_sides_die = Die(10)
for _ in range(20):
    print(ten_sides_die.roll_die())

lottery_pool = [10, 2, 6, 5, 8, 3, 85, 84, 45, 45, 68, 'a', 'b', 'c', 'd']
winning_combination = random.choices(lottery_pool, k=4)
if winning_combination == [2, 6, 5, 8]:
    print("Congratulations, you've won!")
else:
    print(f"Your lottery number is {winning_combination}. You are unlucky. Let's do it again!")

# 创建一个包含 10 个数字和 5 个字母的列表
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

# 定义你的中奖号码
my_ticket = [1, 'B', 3, 'C']

# 初始化循环次数
attempts = 0

# 开始循环，不断随机选择直到和 my_ticket 匹配
while True:
    # 随机生成一组彩票号码
    random_ticket = random.sample(lottery_pool, 4)

    # 增加循环计数
    attempts += 1

    # 如果随机生成的彩票与 my_ticket 匹配，则中奖
    if random_ticket == my_ticket:
        print(f"恭喜！你中奖了！中奖号码是 {random_ticket}")
        print(f"你一共尝试了 {attempts} 次才中大奖！")
        break
