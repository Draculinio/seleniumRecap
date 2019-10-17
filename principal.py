from selenium import webdriver
import unittest
import time
from pages.pageindex import *
from pages.pageitemlist import *
from pages.pageitem import *
class Items(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        self.driver.get('http://automationpractice.com/index.php')

    #def test_do_nothing(self):
    #    pass

    def test_view_item_page(self):
        page_index = Page_index(self.driver)
        page_item_list = Page_item_list(self.driver)
        page_item = Page_item(self.driver)
        page_index.search_items('dress')
        page_item_list.click_first_item()
        page_item.verify_text('Printed Summer Dress')

    def test_search_with_no_items(self):
        page_index = Page_index(self.driver)
        page_index.search_items('computer')

    def tearDown(self):
        self.driver.quit()

#time.sleep(5)

if __name__ == '__main__':
    unittest.main()