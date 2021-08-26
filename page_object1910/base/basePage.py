


class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.base_url = 'http://127.0.0.1:8089'

    def url_find_element(self,loc):
        return self.driver.find_element(*loc)


