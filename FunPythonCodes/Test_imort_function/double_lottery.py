import math


# 计算组合数的函数
def combination(n, k):
    return math.comb(n, k)


total_probability = combination(33, 6)*combination(16, 1)
print(f"1/{total_probability}")

second = combination(33, 6) * combination(16, 0)
print(f"1/{second}")

print(combination(16, 0))