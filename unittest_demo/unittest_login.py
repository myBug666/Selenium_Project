import time
import unittest
from selenium import webdriver

class login(unittest.TestCase):

    # 打开浏览器
    def setUp(self) -> None:
        self.driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # 结束
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    # 登录
    def test_login(self):
        self.driver.get('http://127.0.0.1:8089/index.php?m=user&c=public&a=login')
        self.driver.find_element_by_css_selector('#username').send_keys('tjc123456')
        self.driver.find_element_by_css_selector('#password').send_keys('123456')
        self.driver.find_element_by_css_selector('[value="登　录"]').click()
        time.sleep(3)
        # text = self.driver.find_element_by_link_text('您好')
        text1 = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/a[1]')
        print(text1.text)
        # ***********************************************
        # 验证是否登录的.是否一致
        # self.assertEqual('您好 tjc123456',text1.text)
        # 用用户名去判断
        self.assertIn('tjc123456',text1.text)

if __name__ == '__main__':
    unittest.main()


