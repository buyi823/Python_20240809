# -*- coding: utf-8 -*-
"""
Created on August 21, 2024,
Author: Blaine
Description:
给Battery类添加一个名为upgrade_battery()的方法。
"""


# 这个代码来源ChatGPT

# 定义 Car 类
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# 定义 Battery 类
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    # 获取电池续航范围的方法
    def get_range(self):
        if self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = 240

        print(f"This car can go approximately {range_miles} miles on a full charge.")

    # 升级电池容量的方法
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")
        else:
            print("Battery is already upgraded.")


# 定义 ElectricCar 类，继承自 Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # 创建一个 Battery 实例，作为 ElectricCar 的属性


# 创建 ElectricCar 的实例
my_tesla = ElectricCar("Tesla", "Model S", 2022)

# 显示车辆信息
my_tesla.describe_car()

# 调用电池的 get_range 方法，查看当前电池的续航里程
my_tesla.battery.get_range()

# 升级电池后，再次查看续航里程
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
