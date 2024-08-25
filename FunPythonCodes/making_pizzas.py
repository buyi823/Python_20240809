"""
Created on August 20, 2024
Author: Blaine
Description: Test module import function
"""
# 格式  module_name.function_name()
# 导入特定的函数
# from module_name import function_name
# from module_name import function_0, function_1, function_2
# 如果只想导入使用的函数，可以如下：
# from pizza import make_pizza

# 使用as给函数制定别名
# from module_name import function_name as fn
from pizza import make_pizza as mp
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用as给模块指定别名
# import module_name as mn
import pizza as p

p.make_pizza(16, 'pepperoni')

# 导入模块中的所有函数
# from pizza import *
