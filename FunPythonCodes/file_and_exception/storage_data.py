# -*- coding: utf-8 -*-
"""
Created on August 24, 2024,
Author: Blaine
Description: practice storing data
"""

import json
from datetime import datetime

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


# 这段代码将字典 data 序列化为 JSON 并写入到 data.json 文件中。
data = {"name": "John", "age": 30, "city": "New York"}

# 打开文件，并写入 JSON 数据
with open('data.json', 'w') as file:
    json.dump(data, file)

# 此时生成的 data.json 文件会以 4 个空格缩进的格式显示数据，使其更具可读性。
data = {"name": "John", "age": 30, "city": "New York"}

# 将数据以缩进格式化输出到文件中
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# 输出非 ASCII 字符
# 文件会直接输出中文，而不是将中文转义为 \uXXXX 格式。
data = {"name": "张三", "age": 25, "city": "北京"}

# 使用 ensure_ascii=False，保持中文输出
with open('data.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


# default 参数使用
# 这段代码将 datetime 对象转换为 ISO 格式的字符串输出到 JSON 文件中。

data = {"name": "John", "joined": datetime.now()}


# 自定义函数用于处理无法序列化的对象
def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


# 使用 default 参数处理 datetime 类型
with open('data.json', 'w') as file:
    json.dump(data, file, default=convert_datetime, indent=4)
