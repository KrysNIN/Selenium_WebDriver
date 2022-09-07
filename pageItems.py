from selenium.webdriver.common.by import By

class PageItems ():
    
    def __init__(self, driver):
        self.driver = driver
        self.no_results_banner = '//*[@id="center_column"]/p'
        self.tittle_banner = '//*[@id="center_column"]/h1/span[1]'

    def return_no_element_text(self):
        return self.driver.find_element (By. XPATH, (self.no_results_banner)).text

    def return_section_title(self):
        return self.driver.find_element (By. XPATH, (self.tittle_banner)).text