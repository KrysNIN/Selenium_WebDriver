import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pageIndex import PageIndex
from pageItems import PageItems

class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver_service = Service(executable_path='C:/WebDriver/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)

    def test_search_no_elements(self):                
        self.indexPage.search('Hola')
        time.sleep(5)
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "Hola"')
            
    def test_search_find_dresses(self):
        self.indexPage.search('Dress')
        time.sleep(5)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())
            
    def test_search_find_tshirts(self):        
        self.indexPage.search('T-SHIRTS')
        time.sleep(5)
        self.assertTrue('T-SHIRTS' in self.itemsPage.return_section_title())
            
    def tearDown(self):
        self.driver.close
        self.driver.quit

if __name__ == '__main__':
    unittest.main()