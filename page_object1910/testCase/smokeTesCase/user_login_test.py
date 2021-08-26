import time
import unittest


from page_object1910.base.myTestCase import MyTestCase
from page_object1910.pageObject.loginpage import LoginPage


class test_LoginTest(MyTestCase):
    # 打开url的方法
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.open()
        lp.input_username()
        lp.input_password()
        lp.click_login_btn()
        lp.get_user_info()
                          # 驱动，5s，每0.1秒检查一次
        # WebDriverWait(self.driver,5,0.1).until(expected_conditions.url_changes)
        time.sleep(1.5)
        self.assertIn('我的会员中心',self.driver.title)  # 是否包含
        # self.assertEqual()   是否同等
        # self.assertIn() # 是否包含



if __name__ == '__main__':
    unittest.main()
