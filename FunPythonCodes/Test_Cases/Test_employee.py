import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):


    def setUp(self):
        self.blaine = Employee("Blaine", 65_000)

    def test_give_default_raise(self):
        self.blaine.give_raise()
        self.assertEqual(self.blaine.annual_salary, 70000)

    def test_give_custom_rasie(self):
        self.blaine.give_raise(10000)
        self.assertEqual(self.blaine.annual_salary, 75000)


if __name__ == '__main__':
    print("test start")
    unittest.main(verbosity=2)