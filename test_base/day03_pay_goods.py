import time
from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.maximize_window() # 窗口最大化
driver.implicitly_wait(5) # 隐式等待，只需上面写一次，下面遇到加载情况

# 1、登录
# 输入网址
driver.get('http://127.0.0.1:8089/index.php?m=user&c=public&a=login')
# 输入用户名
time.sleep(1)
driver.find_element_by_css_selector('#username').clear()
driver.find_element_by_css_selector('#username').send_keys('tjc123456')
# 输入密码
driver.find_element_by_css_selector('#password').clear()
driver.find_element_by_css_selector('#password').send_keys('123456')
# 点击登录
driver.find_element_by_css_selector('.login_btn').click()
# 时间等待
time.sleep(3)
# 2、点击进入商城购物
driver.find_element_by_link_text('进入商城购物').click()
# 3、点击商品图片进入详情页
# driver.switch_to.window(driver.window_handles[-1])
driver.find_elements_by_css_selector('.module_pro_img')[0].click()
# 4、点击加入购物车
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_id('joinCarButton').click()
# 5、点击去购物车结算
driver.find_element_by_css_selector('.shopCar_T_span3').click()
# 6、点击结算
driver.find_element_by_css_selector('.shopCar_btn_03').click()
# 7、点击添加新地址
driver.find_element_by_css_selector('.add-address').click()
# 8.1、输入收货人
driver.find_element_by_name('address[address_name]').clear()
driver.find_element_by_name('address[address_name]').send_keys('田建朝')
# 8.2、输入手机号
driver.find_element_by_name('address[mobile]').clear()
driver.find_element_by_name('address[mobile]').send_keys('13812345670')
# 8.3、选择收货地区
# driver.find_element_by_css_selector('#add-new-area-select').clear()
# 河北省
driver.find_element_by_css_selector('#add-new-area-select').click()
driver.find_element_by_css_selector('[value="130000"]').click()
driver.find_element_by_css_selector('#add-new-area-select').click()
# 邯郸市
driver.find_element_by_css_selector('.add-new-area-select').click()
driver.find_element_by_css_selector('[value="130400"]').click()
driver.find_element_by_css_selector('.add-new-area-select').click()
# 魏县
driver.find_element_by_css_selector('.add-new-area-select').click()
driver.find_element_by_css_selector('[value="130434"]').click()
driver.find_element_by_css_selector('.add-new-area-select').click()
# 8.4、输入详细地址
driver.find_element_by_name('address[address]').send_keys('乱几把找')
# 8.5、输入邮政编码
driver.find_element_by_name('address[zipcode]').send_keys('6666')
# 8.5、点击确定
driver.find_element_by_css_selector('.aui_state_highlight').click()

time.sleep(6)
# driver.quit()



