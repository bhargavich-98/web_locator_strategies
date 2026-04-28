# <button class="btn_123 login_btn primary">Login</button>

# 🎯 Task

# Write:

# XPath using text
# XPath using contains()
# CSS selector

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//button[text()='Login']")
driver.find_element(By.XPATH, "//button[contains(@class, 'login_btn')]")
driver.find_element(By.CSS_SELECTOR, ".login_btn")
driver.find_element(By.CSS_SELECTOR, "button.login_btn")
driver.find_element(By.CSS_SELECTOR, "button[class*='login_btn']")
