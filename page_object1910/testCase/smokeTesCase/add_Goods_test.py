import time
import unittest

import ddt
from page_object1910.base.myTestCase import MyTestCase
from page_object1910.func.conn_mysql.delete_record_form_db import Delete_Record_Form_Db
from page_object1910.func.conn_mysql.select_user_info import Select_User_Info
from page_object1910.func.readCsvFile import read
from page_object1910.pageObject.add_goods_page import Add_Goods_Page

@ddt.ddt()
class Add_Goods_Test(MyTestCase):
    test_data = read('add_goods.csv')
    @ddt.data(*test_data)
    @ddt.unpack
    def test_addGoods(self,username,password,userver,addto,textinput,brief):
        lp = Add_Goods_Page(self.driver)
        lp.open()
        lp.input_username(username)
        lp.input_password(password)
        lp.input_userverify(userver)
        lp.click_btn()
        lp.click_set()
        lp.add_goods()
        lp.add_to_goodsuser(addto)
        lp.click_goods_class1()
        lp.click_goods_class2()
        lp.click_goods_class3()
        lp.double_click_iphone()
        lp.goods_select()
        lp.status()
        lp.click_is()
        lp.textInput(textinput)
        lp.briefInput(brief)
        lp.click_submit()

        time.sleep(2)
        user_info = Select_User_Info(addto)
        self.assertEqual(user_info[1],addto)
        print(addto,'0000000000000000')
        time.sleep(2)
        Delete_Record_Form_Db(addto)





if __name__ == '__main__':
    unittest.main()
