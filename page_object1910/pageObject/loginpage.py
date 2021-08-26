# page页放的都是元素定位
from selenium.webdriver.common.by import By
from page_object1910.base.basePage import BasePage
from page_object1910.pageObject.chenge_user_info_page import Change_User_Info_Page


class LoginPage(BasePage):
    # 元素的定位，在登录页面，需要哪些元素，在此定位所需元素
    # 输入框     By 通过什么去定位
    username_input_loc = (By.CSS_SELECTOR,'#username')
    password_input_loc = (By.CSS_SELECTOR,'#password')
    login_btn_loc = (By.CSS_SELECTOR,'[value="登　录"]')
    url = '/index.php?m=user&c=public&a=login'
    user_info = (By.PARTIAL_LINK_TEXT,'您好')

    # 元素操作
    def open(self):  # 打开浏览器
        self.url = self.base_url + self.url
        self.driver.get(self.url)

    # 元素定位的方法
    def input_username(self):
        # self.username_input_loc 是一个元组
        # 加上*号，说明在find_element（）方法中传入的不是一个元组，而是两个元素
        # 因为find_element（）接受两个参数，所以我们不能直接传入元组
        # 应该把元组拆分成两个元素
        self.driver.find_element(*self.username_input_loc).send_keys('tjc123456')

    def input_password(self):
        self.driver.find_element(*self.password_input_loc).send_keys('123456')

    def click_login_btn(self):
        self.driver.find_element(*self.login_btn_loc).click()

    def get_user_info(self):
        self.driver.find_element(*self.user_info)

    def login(self):
        self.open()
        self.input_username()
        self.input_password()
        self.click_login_btn()

        return Change_User_Info_Page(self.driver)



