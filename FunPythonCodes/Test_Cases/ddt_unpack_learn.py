# -*- coding: utf-8 -*-
"""
Created on August 30, 2024,
Author: Blaine
Description: ddt unpack learn
"""

import unittest

from ddt import ddt, data, unpack


@ddt
class DataNums(unittest.TestCase):
    @data([1, 2, 3])  # 列表
    @unpack  # 需要三个参数接收
    def test(self, p1, p2, p3):
        print(p1)
        print(p2)
        print(p3)

    @data({'name': 'bugchen', 'age': 18}, {'name': 'chen', 'age': 28})
    @unpack
    def test_06(self, name, age):
        print(name)
        print(age)


if __name__ == '__main__':
    unittest.main()
