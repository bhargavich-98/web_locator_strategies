# <input type="password" name="password" class="input-field secure" placeholder="Enter password">
# Write:

# Name locator
# CSS selector
# XPath


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.NAME, "password")
driver.find_element(By.CSS_SELECTOR, "input[name='password']")
driver.find_element(By.XPATH, "//input[@name='password']")
