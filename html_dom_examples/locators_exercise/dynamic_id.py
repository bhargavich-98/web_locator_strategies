# <input type="text" id="user_4589_xyz" class="input">

# Write:

# XPath using contains()
# CSS selector

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//input[contains(@id, 'user_')]")
driver.find_element(By.CSS_SELECTOR, "input[id*='user_']")