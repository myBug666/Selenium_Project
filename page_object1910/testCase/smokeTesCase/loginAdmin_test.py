import time
import unittest

from page_object1910.base.myTestCase import MyTestCase
from page_object1910.pageObject.loginadminPage import AdminLogin

# 可维护性高 元素定位于页面分离

class LoginAdmin(MyTestCase):
    def test_admin_login(self):
        ad = AdminLogin(self.driver)
        ad.open()
        ad.input_username()
        ad.input_password()
        ad.input_userverify()
        ad.admin_login_btn()
        # ad.get_user_info()

        time.sleep(3)
        # 断言  title长用assertIn
        self.assertIn('后台管理中心',self.driver.title)

        # self.assertEqual()  # 判断是否同等


# 对于自动化，每一条用例必须有断言
# 登录加上断言，叫半自动测试

if __name__ == '__main__':
    unittest.main()

