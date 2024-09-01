# -*- coding: utf-8 -*-
"""
Created on August 30, 2024,
Author: Blaine
Description: ddt practice
"""

import unittest

from ddt import ddt, data


@ddt  # 类装饰器，表示要使用ddt框架
class DataSend(unittest.TestCase):
    # 传递数字, 传递几个值，方法就执行几次
    @data(10,11)
    def test01_send_int(self, parma1):
        print(parma1)

    @data("string")
    def test02_send_string(self, param1):
        print(param1)

    @data((1,2,3))
    def test03_send_tuple(self, param1):
        print(param1)

    @data([4,5,6,7])
    def test04_send_list(self, parma1):
        print(parma1)

    @data({'name':'blaine', 'age':40})
    def test05_send_dictionary(self, parma1):
        print(parma1)

if __name__ == '__main__':
    unittest.main()
