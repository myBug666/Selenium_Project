'''
注册的基础页面
'''

from selenium.webdriver.common.by import By
from page_object1910.base.basePage import BasePage

class Reg_Page(BasePage):
    url = '/index.php?m=user&c=public&a=reg'
    username_input_loc = (By.NAME,'username')
    password_input_loc = (By.NAME,'password')
    password2_input_loc = (By.NAME,'userpassword2')
    mobile_input_loc = (By.NAME,'mobile_phone')
    email_input_loc = (By.NAME,'email')
    reg_btn_loc = (By.CSS_SELECTOR,'[value="注册"]')

    err_msgs = (By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/form/ul/li/div/span')
    # / html / body / div[3] / div / div[2] / div[1] / form / ul / li[1] / div / span
    # 请填写用户名
    # 用户名不低于三位，使用中文、数字、字母皆可！
    # 密码范围在6~15位之间！

    # 元素操作
    def open(self): # 打开浏览器方法
        self.url = self.base_url + self.url  # 拼接url
        self.driver.get(self.url) # 对url进行操作

    # 元素定位
    # def input_username(self):  # 对用户名操作
    #     self.driver.find_element(*self.username_input_loc).send_keys('akins20')
    def input_username(self,username):  # 对用户名操作,为了实现脚本数据驱动，需要把用变量执行替换固定值
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password):  # 密码操作
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def input_password2(self,userpassword2):  # 密码操作
        self.driver.find_element(*self.password2_input_loc).send_keys(userpassword2)

    def input_mobile(self,mobile_phone):    # 输入手机号
        self.driver.find_element(*self.mobile_input_loc).send_keys(mobile_phone)

    def input_email(self,email):    # 输入邮箱操作
        self.driver.find_element(*self.email_input_loc).send_keys(email)

    def click_reg_btn(self):   # 点击注册btn
        self.driver.find_element(*self.reg_btn_loc).click()

    def get_error_msg(self,err_loc):
        i = int(err_loc) - 1  # -1下标1是0     # 获取完后不是要里面的文字，是要它的文本
        return self.driver.find_elements(*self.err_msgs)[i].text
