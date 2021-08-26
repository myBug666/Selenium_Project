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
# 点击商品管理
driver.find_element_by_link_text('商品管理').click()
# 点击添加商品
driver.find_element_by_link_text('添加商品').click()
# 输入商品
driver.switch_to.frame('mainFrame')
driver.find_element_by_name('name').send_keys('iPhone666')
# 商品分类
driver.find_element_by_id('1').click()
ele = driver.find_element_by_id('3')
ActionChains(driver).double_click(ele).perform()
driver.find_element_by_id('2').click()
driver.find_element_by_id('6').click()
ele = driver.find_element_by_css_selector('[id="7"]')
ActionChains(driver).double_click(ele).perform()
# 选择商品品牌
goods = driver.find_element_by_name('brand_id')
Select(goods).select_by_visible_text('苹果 (Apple)')
# 选择是否上架
driver.find_element_by_css_selector('[name="status"][value="1"]').click()
# 点击商品图册
driver.find_element_by_link_text('商品图册').click()
# 上传图片                                  注意转义字符  必须来一个转义\
driver.find_element_by_name('file').send_keys('D:\\1.png')
# 点击上传
driver.find_element_by_xpath('//*[@id="uploader"]/div[2]/div[3]/div[2]').click()
# 点击弹框
time.sleep(1)
alt = driver.switch_to.alert.text
print(alt)
driver.switch_to.alert.accept() # 点击弹框确定
# 点击提交
driver.find_element_by_css_selector('[value="提交"]').click()
time.sleep(6)
driver.quit()


