"""
双色球是一种彩票游戏，其中玩家需要从 33 个红球 中选择 6 个不重复的号码，
并从 16 个蓝球 中选择 1 个蓝色号码。中奖分为多个奖项，通常根据匹配的红球和蓝球数量来决定。
奖项设置
以下是常见的奖项设置（以中国双色球为例），根据匹配的红球和蓝球数量来决定中奖等级：
一等奖：6 个红球 + 1 个蓝球
二等奖：6 个红球 + 0 个蓝球
三等奖：5 个红球 + 1 个蓝球
四等奖：5 个红球 + 0 个蓝球 或 4 个红球 + 1 个蓝球
五等奖：4 个红球 + 0 个蓝球 或 3 个红球 + 1 个蓝球
六等奖：2 个红球 + 1 个蓝球 或 1 个红球 + 1 个蓝球 或 0 个红球 + 1 个蓝球
计算概率
1. 组合公式
我们需要使用组合数学公式计算概率。组合的公式为：
C(n,k)=n!/k!(n-k)!
其中，C(n, k) 表示从 n 个元素中选取 k 个元素的组合数量。
C(33, 6) 表示从 33 个红球中选择 6 个红球的组合数。
C(16, 1) 表示从 16 个蓝球中选择 1 个蓝球的组合数。
2. 计算总的可能组合数
总的可能组合数为：

总组合数
总组合数=C(33,6)×C(16,1)
"""

import math


# 计算组合数的函数
def combination(n, k):
    return math.comb(n, k)


# 计算各个奖项的概率
def calculate_probabilities():
    # 总的组合数：C(33, 6) * C(16, 1)
    total_combinations = combination(33, 6) * combination(16, 1)

    # 一等奖：6 红 + 1 蓝
    first_prize = 1 / (combination(33, 6) * combination(16, 1))

    # 二等奖：6 红 + 0 蓝
    second_prize = 1 / combination(33, 6)

    # 三等奖：5 红 + 1 蓝
    third_prize = 1 / (combination(33, 5) * combination(16, 1))

    # 四等奖：5 红 + 0 蓝 或 4 红 + 1 蓝
    fourth_prize = 1 / combination(33, 5) + 1 / (combination(33, 4) * combination(16, 1))

    # 五等奖：4 红 + 0 蓝 或 3 红 + 1 蓝
    fifth_prize = 1 / combination(33, 4) + 1 / (combination(33, 3) * combination(16, 1))

    # 六等奖：2 红 + 1 蓝 或 1 红 + 1 蓝 或 0 红 + 1 蓝
    sixth_prize = 1 / (combination(33, 2) * combination(16, 1)) + 1 / (
            combination(33, 1) * combination(16, 1)) + 1 / combination(16, 1)

    # 打印中奖概率和每多少次投注中有一次中奖
    print(f"一等奖概率：{first_prize:.10f}，即约 1/{int(1 / first_prize):,} 次")
    print(f"二等奖概率：{second_prize:.10f}，即约 1/{int(1 / second_prize):,} 次")
    print(f"三等奖概率：{third_prize:.10f}，即约 1/{int(1 / third_prize):,} 次")
    print(f"四等奖概率：{fourth_prize:.10f}，即约 1/{int(1 / fourth_prize):,} 次")
    print(f"五等奖概率：{fifth_prize:.10f}，即约 1/{int(1 / fifth_prize):,} 次")
    print(f"六等奖概率：{sixth_prize:.10f}，即约 1/{int(1 / sixth_prize):,} 次")


# 调用函数计算双色球各奖项概率
calculate_probabilities()
