import unittest
from my_unit import MyUnit
# 新建一个类必须继承unittest.TestCase

class TestApi(MyUnit):
    age = 16
    # 方法必须以test_开头
    def test_mashang(self):
        print("test")

    def test_blaine(self):
        print("This is unit test!")

    def test_blaine_001(self):
        print("001This is unit test!")

    def test_blaine_002(self):
        print("002This is unit test!")

    def test_failed(self):
        self.assertTrue(False)

    def test_exception(self):
        print("以下测试异常")
        raise Exception("这里测试异常")

    @unittest.skip(reason="test")
    def test_skip(self):
        print("测试跳过")

    @unittest.skipIf(age < 18, "条件为true, skip")
    def test_skip_true(self):
        print("test has been skipped!")

    @unittest.skipUnless(age > 18, "条件为假，跳过")
    def test_skip_false(self):
        print("skip！")


if __name__ == '__main__':
    print("test start")
    # 执行时要指定套件
    unittest.main(verbosity=2)
