import unittest


class NameRule1(unittest.TestCase):
    # 执行成功
    def test01(self):
        print('test1')

    # 执行错误
    def test02(self):
        print('test2')
        raise Exception("执行错误")

    # 执行跳过
    @unittest.skip('跳过')
    def test11(self):
        print('test11')

    # 执行失败
    def test12(self):
        self.assertTrue(0)  # 0不为True
        print('test12')


if __name__ == '__main__':
    print('=============main================')
    unittest.main()

