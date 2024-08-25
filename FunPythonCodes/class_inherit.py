# -*- coding: utf-8 -*-
"""
Created on August 20, 2024,
Author: Blaine
Description: This is my exercise in class inheritance.
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电池电量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315

        print(f"This car can go about {range_miles} miles on a full charge.")


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
