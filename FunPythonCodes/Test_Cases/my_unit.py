import unittest


"""fixture的封装"""
class MyUnit(unittest.TestCase):
    def setUp(self) -> None:
        print("在每一个测试用例之前执行")

    def tearDown(self) -> None:
        print("在每一个测试用例之后执行")

    @classmethod
    def setUpClass(cls) -> None:
        print("在每个类之前执行。")
    @classmethod
    def tearDownClass(cls) -> None:
        print("在每个类之后执行")