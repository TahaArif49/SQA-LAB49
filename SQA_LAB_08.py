#03

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org")
links = driver.find_elements(By.TAG_NAME, "a")
total_links = len(links)
print("Total Links Wikipedia:", total_links)
driver.quit()


#04
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
username_id = driver.find_element(By.ID, "username")
print("Username field found using ID.")
username_name = driver.find_element(By.NAME, "username")
print("Username field found using NAME.")
username_css = driver.find_element(By.CSS_SELECTOR, "#username")
print("Username field found using CSS Selector.")
time.sleep(10)
driver.quit()

#05

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")
text_inputs = driver.find_elements(
    By.CSS_SELECTOR, 'input[type="text"]'
)
print("Total Text Input Fields:", len(text_inputs))
for field in text_inputs:
    print("Input ID:", field.get_attribute("id"))
    print("Input Name:", field.get_attribute("name"))
time.sleep(5)
driver.quit()

#06
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_tables.asp")
xpath = '//table[@id="customers"]//tr[3]/td[2]'
cell = driver.find_element(By.XPATH, xpath)
print("Text of the Table Cell:", cell.text)
time.sleep(10)
driver.quit()
