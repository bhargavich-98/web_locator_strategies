# <input type="text" id="username" name="user_email" class="input-field form-control">
# Write 3 locators:

# Best locator
# CSS selector
# XPath

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.ID, "username")
driver.find_element(By.CSS_SELECTOR, "input#username")
driver.find_element(By.CSS_SELECTOR, "#username")
driver.find_element(By.XPATH, "//input[@id='username']")

