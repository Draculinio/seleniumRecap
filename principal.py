from selenium import webdriver
import unittest
import time
from pages.pageindex import *

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
        page_index.search_items('dress')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img').click()
        title = self.driver.find_element_by_xpath('//h1[@itemprop="name"]').text
        self.assertEqual(title, 'Printed Summer Dress', 'Text should be different')

    def test_search_with_no_items(self):
        page_index = Page_index(self.driver)
        page_index.search_items('computer')

    def tearDown(self):
        self.driver.quit()

#time.sleep(5)

if __name__ == '__main__':
    unittest.main()