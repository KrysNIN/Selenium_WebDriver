from selenium.webdriver.common.by import By

class PageIndex ():

    def __init__(self, driver ):
        self.query_top = "search_query_top"
        self.query_button = "submit_search"
        self.driver = driver

    def search(self, item):
        self.driver.find_element (By. ID, (self.query_top)).send_keys(item)
        self.driver.find_element (By. NAME, (self.query_button)).click()