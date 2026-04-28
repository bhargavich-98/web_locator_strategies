# <ul>
#   <li class="item">Item 1</li>
#   <li class="item">Item 2</li>
#   <li class="item">Item 3</li>
# </ul>

# 🎯 Task

# Write:

# XPath for Item 2
# XPath using index
# CSS selector

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.XPATH, "//li[text()='Item 2']")
driver.find_element(By.XPATH, "(//li[@class='item'])[2]")
driver.find_element(By.CSS_SELECTOR, "li.item:nth-child(2)")
driver.find_element(By.CSS_SELECTOR, "li.item:nth-of-type(2)")