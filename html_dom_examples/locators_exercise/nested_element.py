# <div class="login-form">
#     <input type="text" name="email">
# </div>

# 🎯 Task

# Write:

# XPath using parent → child
# CSS selector

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.XPATH,  "//div[@class='login-form']/input[@name='email']")
driver.find_element(By.CSS_SELECTOR, "div.login-form > input[name='email']")
driver.find_element(By.XPATH, "//div[@class='login-form']//input[@name='email']")