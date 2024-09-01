import unittest

def setUpModule():
    print('setUpAndtearDown.py模块之前')

def tearDownModule():
    print('setUpAndtearDown.py模块之后')


class ErpLogin1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("在Class之前运行,一般用于连接数据库")

    @classmethod
    def tearDownClass(self):
        print("在Class之后运行，一般关闭数据库连接以及一些日志对象的销毁")

    def setUp(self):
        print("每个方法前执行，如打开浏览器")

    def tearDown(self):
        print("每个方法后执行，如业务完成关闭浏览器")

    def test01_login(self):
        print('erp管理系统的login（登录）测试')

    def test02_loginCheckParam(self):
        print('erp管理系统login登录参数验证测试')

    def test03_addUser(self):
        print('erp管理系统addUser新增用户测试')

    @unittest.skip(reason="no any reason, just wanna skip this test case.")
    def test_skip(self):
        print("测试跳过")

    @unittest.skipIf(2>1, reason="True skip")
    def test_skip(self):
        print("为真跳过,为假执行")


if __name__ == '__main__':
    print('==========erp管理系统登录模块的验证===================')
    # 只完成登录参数校验的验证测试和登录的测试
    # 第一种方法，在main方法中指定需要测试测试方法
    # unittest.main(defaultTest=['ErpLogin1.test02_loginCheckParam','ErpLogin1.test01_login'])

    # 第二种方法 采用测试套件TestSuit
    # testSuit = unittest.TestSuite()
    # 添加需要的测试方法
    # testSuit.addTest(test=ErpLogin1('test01_login'))
    # testSuit.addTest(ErpLogin1('test03_addUser'))
    # # 使用addTests
    # testcase = [ErpLogin1('test01_login'), ErpLogin1('test03_addUser')]
    # testSuit.addTests([ErpLogin1('test01_login'), ErpLogin1('test03_addUser')])
    # testSuit.addTests(testcase)
    # 执行测试方法，将测试的结果使用文本的方式打印出来
    # unittest.TextTestRunner().run(testSuit)

    # 第三种方法，通过类加载器的方式来实现
    suit = unittest.TestSuite()
    testMethods = unittest.defaultTestLoader.discover(
        start_dir=r'D:\Source codes\Python_20240809\FunPythonCodes\Python_test_codes',
        pattern='*_login.py')
    suit.addTest(testMethods)
    unittest.main(verbosity=2)
    # unittest.main(defaultTest='testSuit', verbosity=2)
