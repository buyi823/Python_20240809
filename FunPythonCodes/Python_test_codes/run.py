import unittest

from FunPythonCodes.Python_test_codes import TestApi
from FunPythonCodes.Python_test_codes import TestWeb

if __name__ == "__main__":
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 把测试用例加载到测试套件里面
    suite.addTest(TestApi('test_blaine'))
    suite.addTest(TestApi('test_mashang'))
    suite.addTest(TestWeb('test_web'))

    # 多个用例的方式
    testcases = [TestApi('test_blaine'), TestApi('test_mashang'), TestWeb('test_web')]
    suite.addTests(testcases)
    # 以上是测试套件加载器的方式加载

    # 测试加载器的方式加载

    unittest.main(defaultTest='suite')



