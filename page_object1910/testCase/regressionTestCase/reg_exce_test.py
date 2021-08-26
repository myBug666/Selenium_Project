import time
import unittest


from page_object1910.base.myTestCase import MyTestCase
from page_object1910.func.get_screenshot import Get_Screenshot
from page_object1910.func.readCsvFile import read
from page_object1910.pageObject.reg_page import Reg_Page
import ddt

# 添加ddt修饰类
@ddt.ddt()
class Reg_Normal_Test(MyTestCase):
    test_data = read('reg_exce.csv')

    @ddt.data(*test_data)

    @ddt.unpack
    def test_reg(self,username,password,userpassword2,mobile_phone,email,err_msg,err_loc):
        rp = Reg_Page(self.driver) # 驱动
        rp.open()
        rp.input_username(username)
        rp.input_password(password)
        rp.input_password2(userpassword2)
        rp.input_mobile(mobile_phone)
        rp.input_email(email)
        rp.click_reg_btn()
        time.sleep(2)
        actual = rp.get_error_msg(err_loc)
        Get_Screenshot(self.driver,'注册异常用例')
        # 断言
        self.assertEqual(err_msg,actual)
        print('实际结果,'+actual+',期望结果：' + err_msg)



if __name__ == '__main__':
    unittest.main()
