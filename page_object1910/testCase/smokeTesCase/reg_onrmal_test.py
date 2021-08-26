import time
import unittest


from page_object1910.base.myTestCase import MyTestCase
from page_object1910.func.conn_mysql.delete_record_form_db import Delete_Record_Form_Db
from page_object1910.func.conn_mysql.select_user_info import Select_User_Info
from page_object1910.func.readCsvFile import read
from page_object1910.pageObject.reg_page import Reg_Page
import ddt

# 添加ddt修饰类
@ddt.ddt()
class Reg_Normal_Test(MyTestCase):
    test_data = read('reg_normal.csv')
    # 为测试方法添加修饰器
    @ddt.data(*test_data)
    # 修改方法的参数列表
    # 每次去掉一行数据，通过unpack，可以把每一行数据，分解为多个单元格
    @ddt.unpack  # 读取一行取消一行
    def test_reg(self,username,password,userpassword2,mobile_phone,email):
        rp = Reg_Page(self.driver) # 驱动
        rp.open()
        # rp.input_username()  # page页里使用变量，此处需要传值
        rp.input_username(username)
        rp.input_password(password)
        rp.input_password2(userpassword2)
        rp.input_mobile(mobile_phone)
        rp.input_email(email)
        rp.click_reg_btn()
        time.sleep(2)
        # 通过用户名查询
        user_info = Select_User_Info(username)
        # 判断第二个---邮箱  断言
        self.assertEqual(user_info[2],email)
        # 先断言是否成功在删除
        Delete_Record_Form_Db(username)



if __name__ == '__main__':
    unittest.main()
