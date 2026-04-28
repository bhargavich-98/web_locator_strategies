# <a href="/product/iphone14" class="product-link">Apple iPhone 14</a>
# 🎯 Task

# Write:

# Link Text
# Partial Link Text
# XPath


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.LINK_TEXT, "Apple iPhone 14")
driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone")
driver.find_element(By.XPATH, "//a[contains(text(), 'iPhone')]")
driver.find_element(By.XPATH, "//a[@href='/product/iphone14']")