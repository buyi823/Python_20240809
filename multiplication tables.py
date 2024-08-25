'''
-*- coding: utf-8 -*-
@File: multiplication table
@author: from the network
@Time: 2023/7/16

'''


# 双重循环
# 使用for循环遍历1到9中的每个数字
for i in range(1, 10):
    # 使用嵌套的for循环遍历1到i+1的每个数字
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t',end='')
    # 打印一个空行，以实现乘法口诀表的垂直排列
    print()

####################################
print('\n')
####################################

# 一行代码实现
print("\n".join(' '.join([f"{j}x{i}={i*j}" for j in range(1, i+1)]) for i in range(1, 10)))

print('\n')

# 使用列表实现

a = [1,2,3,4,5,6,7,8,9]
for i in a:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print()