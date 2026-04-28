# <span class="a-size-medium a-color-base a-text-normal">
#   Samsung Galaxy S21
# </span>

# 🎯 Task

# Write:

# XPath using text
# XPath using contains()
# CSS selector

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//span[contains(text(), 'Samsung Galaxy S21')]")
driver.find_element(By.XPATH, '//span[text()="Samsung Galaxy S21"]')
driver.find_element(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")

