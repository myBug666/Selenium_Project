'''
封装一些东西
'''
import time
import unittest
from selenium import webdriver
                       # TestCase  引用一些用例
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
        # self.driver = webdriver.Ie()
        # self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)  # 调试期间使用，带脚本稳定后，去除该时间等待
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

