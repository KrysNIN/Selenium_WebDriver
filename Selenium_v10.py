import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_service = Service(executable_path="C:/WebDriver/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get('http://automationpractice.com/index.php')
time.sleep(3)
search_box = driver.find_element (By.ID, "search_query_top")
search_box.send_keys('KrysNIN')
time.sleep(3)
search_box.clear()
search_box = driver.find_element (By.NAME, 'search_query')
search_box.send_keys('Automation')
time.sleep(3)
search_box.clear()
search_box = driver.find_element (By.XPATH, '//*[@id="search_query_top"]')
search_box.send_keys('Rules!')
time.sleep(5)
search_box.clear()
search_box = driver.find_element (By.CLASS_NAME, 'search_query.form-control.ac_input')
search_box.send_keys('Samurai')
time.sleep(2)
search_box.clear()
time.sleep(2)
driver.find_element (By.LINK_TEXT, 'T-SHIRTS').click()
time.sleep(2)
driver.find_element (By.PARTIAL_LINK_TEXT, 'DRESS').click()
time.sleep(5)
driver.close()
driver.quit()