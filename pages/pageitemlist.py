from selenium.webdriver.common.by import By

class Page_item_list:
    def __init__(self, driver):
        self.driver = driver
        self.item = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')

    def click_first_item(self):
        self.driver.find_element(*self.item).click()