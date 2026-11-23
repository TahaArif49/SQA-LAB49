#03

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(5)
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys("Alex")
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys("Thomson")
email = driver.find_element(By.ID, "userEmail")
email.send_keys("pncalexthomson@gmail.com")
gender = driver.find_element(
    By.CSS_SELECTOR, 'label[for="gender-radio-1"]'
)
gender.click()
mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("+923001234567")
print("First Name:", first_name.get_attribute("value"))
print("Last Name:", last_name.get_attribute("value"))
print("Email:", email.get_attribute("value"))
print("Gender Selected:", driver.find_element(
    By.ID, "gender-radio-1"
).is_selected())
print("Mobile Number:", mobile.get_attribute("value"))
driver.quit()


#04

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(5)
checkbox = driver.find_elements(
    By.CSS_SELECTOR, 'input[type="checkbox"]'
)[0]
initial_state = checkbox.is_selected()
print("Initial Checkbox State:", initial_state)
checkbox.click()
time.sleep(4)
after_first_click = checkbox.is_selected()
print("After First Click:", after_first_click)
checkbox.click()
time.sleep(4)
final_state = checkbox.is_selected()
print("After Second Click:", final_state)
if initial_state == final_state:
    print("Result: Checkbox returned to its original state.")
else:
    print("Result: Checkbox state did not return to original.")
driver.quit()


#06
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(5)
male = driver.find_element(By.ID, "gender-radio-1")
female = driver.find_element(By.ID, "gender-radio-2")
other = driver.find_element(By.ID, "gender-radio-3")
driver.find_element(
    By.CSS_SELECTOR, 'label[for="gender-radio-1"]'
).click()
print("Male Selected:", male.is_selected())
print("Female Selected:", female.is_selected())
print("Other Selected:", other.is_selected())
driver.find_element(
    By.CSS_SELECTOR, 'label[for="gender-radio-2"]'
).click()
print("After Selecting Female:")
print("Male Selected:", male.is_selected())
print("Female Selected:", female.is_selected())
print("Other Selected:", other.is_selected())
driver.quit()


#06

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(5)
dropdown_element = driver.find_element(By.ID, "dropdown")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Option 1")
print(
    "Selected by Visible Text:",
    dropdown.first_selected_option.text
)
dropdown.select_by_index(2)
print(
    "Selected by Index:",
    dropdown.first_selected_option.text
)
dropdown.select_by_value("1")
print(
    "Selected by Value:",
    dropdown.first_selected_option.text
)
driver.quit()
