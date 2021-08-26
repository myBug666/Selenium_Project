import time
import unittest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object1910.base.myTestCase import MyTestCase
from page_object1910.pageObject.loginpage import LoginPage


class Change_User_Info_Test(MyTestCase):
    # 必须是test开头的用例
    def test_change_user_info(self):
        lp = LoginPage(self.driver)
        tcui = lp.login()
        tcui.click_setting_account()
        tcui.click_personal_data()
        tcui.input_true_name()
        tcui.click_sex()
        tcui.input_birthday()
        tcui.input_qq()
        tcui.click_btn()

        # WebDriverWait(self.driver,5,0.2).until(expected_conditions.url_changes)
        time.sleep(3)
        alert_text = self.driver.switch_to.alert.text
        self.assertNotEqual('个人信息修改成功！',alert_text)
        # self.assertNotEqual('个人信息修改成功！',alert_text)
        print(alert_text)
        self.driver.switch_to.alert.accept()



if __name__ == '__main__':
    unittest.main()