import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10) # 隐式等待

# 1、登录海盗商城后台
driver.get('http://127.0.0.1:8089/index.php?m=admin&c=public&a=login')
# 输入用户名
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('admin')
# 输入密码
driver.find_element_by_name('userpass').clear()
driver.find_element_by_name('userpass').send_keys('password')
# 输入验证码
driver.find_element_by_name('userverify').clear()
driver.find_element_by_name('userverify').send_keys('1234')
# 点击登录btn
driver.find_element_by_css_selector('.Btn').click()
# 2、点击商品管理
driver.find_element_by_link_text('商品管理').click()
# 3、点击添加商品
driver.find_element_by_link_text('添加商品').click()
# time.sleep(3)
# 4、输入商品名
driver.switch_to.frame('mainFrame')
driver.find_element_by_name('name').send_keys('华为折叠')
# 5.1、选择分类、手机数码通讯
driver.find_element_by_id(1).click()

# 双击id为3的
ele = driver.find_element_by_id(3)
ActionChains(driver).double_click(ele).perform()
# 双击id为5的
ele = driver.find_element_by_id(5)
ActionChains(driver).double_click(ele).perform()
# 5.2、选择手机通讯
driver.find_element_by_id(2).click()
# 5.3、选择手机
driver.find_element_by_id(6).click()
# 5.4、双击选择苹果
ip = driver.find_element_by_id(7)
ActionChains(driver).double_click(ip).perform()
# driver.find_element_by_id(7).click()
# 6、商品品牌选择苹果
goods = driver.find_element_by_name('brand_id')
Select(goods).select_by_visible_text('苹果 (Apple)')
# 7、选择上架销售
# time.sleep(3)
driver.find_elements_by_name('status')[0].click() # 是
# driver.find_elements_by_name('status')[1].click() # 否
# time.sleep(3)
# 8、选择商品状态
driver.find_element_by_name('is_hot').click()
driver.find_element_by_name('is_new').click()
# 商品关键词
driver.find_element_by_name('keyword').send_keys('666商品')
# 商品描述
driver.find_element_by_name('brief').send_keys('此商品为本店最好的商品')
# 9、点击提交
driver.find_element_by_css_selector('[value="提交"]').click()

time.sleep(6)
driver.quit()