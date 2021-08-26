from selenium.webdriver.common.by import By


class Change_User_Info_Page():
    # 元素定位
    setting_account_click_loc = (By.LINK_TEXT,'账号设置')
    personal_data_click_loc = (By.LINK_TEXT,'个人资料')
    ture_name_input_loc = (By.CSS_SELECTOR,'#true_name')
    sex_click_loc = (By.CSS_SELECTOR,'#xb')
    birthday_input_loc = (By.CSS_SELECTOR,'#date')
    qq_input_loc = (By.CSS_SELECTOR,'#qq')
    btn_click_loc = (By.CSS_SELECTOR,'.btn4')

    def __init__(self,driver):
        self.driver = driver

    # 元素操作
    def click_setting_account(self):
        self.driver.find_element(*self.setting_account_click_loc).click()

    def click_personal_data(self):
        self.driver.find_element(*self.personal_data_click_loc).click()

    def input_true_name(self):
        self.driver.find_element(*self.ture_name_input_loc).clear()
        self.driver.find_element(*self.ture_name_input_loc).send_keys('张柳')

    def click_sex(self):
        self.driver.find_elements(*self.sex_click_loc)[1].click()

    def input_birthday(self):
        self.driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
        self.driver.find_element(*self.birthday_input_loc).clear()
        self.driver.find_element(*self.birthday_input_loc).send_keys('1988-08-08')

    def input_qq(self):
        self.driver.find_element(*self.qq_input_loc).clear()
        self.driver.find_element(*self.qq_input_loc).send_keys('123456980')

    def click_btn(self):
        self.driver.find_element(*self.btn_click_loc).click()





