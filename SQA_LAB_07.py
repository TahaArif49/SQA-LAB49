#03
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("Website 1 Title:", driver.title)
print("Website 1 URL:", driver.current_url)
time.sleep(3)
driver.get("https://www.python.org")
print("Website 2 Title:", driver.title)
print("Website 2 URL:", driver.current_url)
time.sleep(3)
driver.get("https://www.wikipedia.org")
print("Website 3 Title:", driver.title)
print("Website 3 URL:", driver.current_url)
time.sleep(3)
driver.back()
time.sleep(3)
driver.back()
time.sleep(3)
print("After Back Twice:", driver.title)
driver.forward()
time.sleep(3)
print("After Forward Once:", driver.title)
driver.quit()

#04


from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)
driver.get("https://www.python.org")
time.sleep(3)
driver.get("https://www.wikipedia.org")
time.sleep(3)
driver.back()
time.sleep(3)
driver.back()
time.sleep(3)
print("title after back twice:", driver.title)
driver.forward()
time.sleep(3)
print("title after forward once:", driver.title)
driver.quit()

#05


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")
time.sleep(2)
title_before = driver.title
print("Title Before Refresh:", title_before)
driver.refresh()
time.sleep(2)
title_after = driver.title
print("Title After Refresh:", title_after)
if title_before == title_after:
    print("Result: Page title remained the same.")
else:
    print("Result: Page title changed.")
driver.quit()

#06


from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
print("First Website Title:", driver.title)
print("First Website URL:", driver.current_url)
time.sleep(3)
driver.get("https://www.smiu.edu.pk")
print("Second Website Title:", driver.title)
print("Second Website URL:", driver.current_url)
time.sleep(3)
driver.back()
time.sleep(3)
print("Title After Back:", driver.title)
driver.forward()
time.sleep(3)
print("Title After Forward:", driver.title)
driver.refresh()
time.sleep(3)
print("Title After Refresh:", driver.title)
driver.quit()
