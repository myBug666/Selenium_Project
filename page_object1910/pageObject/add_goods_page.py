import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page_object1910.base.basePage import BasePage


class Add_Goods_Page(BasePage):
    url = '/index.php?&m=admin&c=public&a=login'
    username_input_loc = (By.NAME,'username')
    password_input_loc = (By.NAME,'userpass')
    # 验证码
    placeholder_input_loc = (By.NAME,'userverify')
    submit_input_loc = (By.CSS_SELECTOR,'.Btn')
    click_set_up = (By.LINK_TEXT,'商品管理')
    click_add_goods = (By.LINK_TEXT,'添加商品')
    # 输入商品名称
    add_to_goods_user = (By.NAME,'name')
    # 点击id为1的 手机、数码、通讯
    goods_class1 = (By.ID,'1')
    # 点击id 2 手机通讯
    goods_class2 = (By.ID,'2')
    # 点击id 6 手机
    goods_class3 = (By.ID,'6')
    # 双击苹果添加标签
    goods_class4 = (By.ID,'7')
    # 商品品牌
    goods_pinpai = (By.NAME,'brand_id')
    # 是否上架
    T_F_status = (By.NAME,'status')
    is_hot = (By.NAME,'is_hot')
    is_new = (By.NAME,'is_new')
    text_input = (By.NAME,'keyword')
    brief_input = (By.NAME,'brief')
    click_submit_btn = (By.CSS_SELECTOR,'[value="提交"]')



    # 元素操作
    def open(self):
        self.url = self.base_url + self.url
        self.driver.get(self.url)

    # 元素定位
    def input_username(self,username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    # 输入密码
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    # 输入验证码
    def input_userverify(self,userver):
        self.driver.find_element(*self.placeholder_input_loc).send_keys(userver)
    # 点击btn
    def click_btn(self):
        self.driver.find_element(*self.submit_input_loc).click()
    # 点击站点设置
    def click_set(self):
        self.driver.find_element(*self.click_set_up).click()
    # 点击添加商品
    def add_goods(self):
        self.driver.find_element(*self.click_add_goods).click()
    # 输入商品名称
    def add_to_goodsuser(self,addto):
        self.driver.switch_to.frame('mainFrame')
        self.driver.find_element(*self.add_to_goods_user).send_keys(addto)
    # 商品分类
    def click_goods_class1(self):
        self.driver.find_element(*self.goods_class1).click()

    def click_goods_class2(self):
        self.driver.find_element(*self.goods_class2).click()

    def click_goods_class3(self):
        self.driver.find_element(*self.goods_class3).click()
    # 双击苹果标签
    def double_click_iphone(self):
        ele = self.driver.find_element(*self.goods_class4)
        ActionChains(self.driver).double_click(ele).perform()
    # 选择品牌
    def goods_select(self):
        time.sleep(1)
        goods = self.driver.find_element(*self.goods_pinpai)
        Select(goods).select_by_visible_text('苹果 (Apple)')
    # 上架销售
    def status(self):
        self.driver.find_elements(*self.T_F_status)[0].click()
    # 商品状态
    def click_is(self):
        self.driver.find_element(*self.is_hot).click()
        self.driver.find_element(*self.is_new).click()
    # 输入商品关键词
    def textInput(self,textinput):
        self.driver.find_element(*self.text_input).send_keys(textinput)
    # 商品描述
    def briefInput(self,brief):
        self.driver.find_element(*self.brief_input).send_keys(brief)
    # 点击提交btn
    def click_submit(self):
        self.driver.find_element(*self.click_submit_btn).click()





