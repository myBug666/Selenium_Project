from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
driver.get('http://127.0.0.1:8089/index.php?&m=admin&c=public&a=login')
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('admin')





