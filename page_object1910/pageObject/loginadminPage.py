from selenium.webdriver.common.by import By

from page_object1910.base.basePage import BasePage


class AdminLogin(BasePage):
    username_input_loc = (By.NAME,'username')
    password_input_loc = (By.NAME,'userpass')
    userverify_input_loc = (By.NAME,'userverify')
    submit_input_loc = (By.CSS_SELECTOR,'.Btn')
    url = '/index.php?m=admin&c=public&a=login'
    # user_info = (By.PARTIAL_LINK_TEXT,'欢迎您')

    # print('123465464646')

    # 元素操作
    def open(self):
        self.url = self.base_url + self.url
        self.driver.get(self.url)

    # 元素定位方法
    def input_username(self):
        self.driver.find_element(*self.username_input_loc).send_keys('admin')

    def input_password(self):
        self.driver.find_element(*self.password_input_loc).send_keys('password')

    def input_userverify(self):
        self.driver.find_element(*self.userverify_input_loc).send_keys('1234')

    def admin_login_btn(self):
        self.driver.find_element(*self.submit_input_loc).click()

    # def get_user_info(self):
    #     self.driver.find_element(*self.user_info)



