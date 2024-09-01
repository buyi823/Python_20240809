import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from FunPythonCodes.Test_Cases.my_unit import MyUnit


class TestEcShop(MyUnit):

    def test_01_edit_product(self):

        driver = webdriver.Chrome()
        # 打开Jenkins
        driver.get("http://localhost:60260/")
        # loging
        driver.find_element(By.NAME, "j_username").send_keys("admin")
        # 密码
        driver.find_element(By.NAME, "j_password").send_keys("admin")
        # sign in 按钮
        driver.find_element(By.NAME, "Submit").click()
