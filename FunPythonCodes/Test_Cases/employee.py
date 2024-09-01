import unittest


class Employee():

    def __init__(self, name, annual_salary):
        self.name = name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount




