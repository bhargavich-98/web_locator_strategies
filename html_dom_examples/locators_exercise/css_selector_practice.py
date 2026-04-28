# <input id="email" class="input form-control" type="text">
# 🎯 Task

# Write:

# ID selector
# Class selector (single class)
# Combined selector (tag + class)


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.find_element(By.ID, "email")
driver.find_element(By.CLASS_NAME, "input")
driver.find_element(By.CSS_SELECTOR, "input.input.form-control")
driver.find_element(By.CSS_SELECTOR, "input.form-control")


# <button class="btn primary login-btn">Login</button>
# 🎯 Task

# Write:

# Selector using all classes
# Selector using only login-btn
# Selector using tag + class

driver.find_element(By.CSS_SELECTOR, "button.btn.primary.login-btn")
driver.find_element(By.CSS_SELECTOR, "button.login-btn")
driver.find_element(By.CSS_SELECTOR, "button[class*='login-btn']")

# <input type="password" name="user_pass" placeholder="Enter password">
# 🎯 Task

# Write:

# Selector using name
# Selector using type
# Selector using both attributes

driver.find_element(By.CSS_SELECTOR, "input[name='user_pass']")
driver.find_element(By.CSS_SELECTOR, "input[type='password']")
driver.find_element(By.CSS_SELECTOR, "input[name='user_pass'][type='password']")


# <button class="btn_login_4589 btn-primary">Login</button>
# 🎯 Task

# Write:

# Selector using partial class match
# Selector using starts-with concept
# Selector using contains concept

driver.find_element(By.CSS_SELECTOR, "button[class*='btn_login']")
driver.find_element(By.CSS_SELECTOR, "button[class^='btn_login']")
driver.find_element(By.CSS_SELECTOR, "button[class*='login']")


# <ul>
#   <li class="item">Item 1</li>
#   <li class="item">Item 2</li>
#   <li class="item">Item 3</li>
# </ul>
# 🎯 Task

# Write:

# Select all items
# Select second item
# Select first item

driver.find_elements(By.CSS_SELECTOR, "li.item")
driver.find_element(By.CSS_SELECTOR, "li.item:nth-of-type(2)")
driver.find_element(By.CSS_SELECTOR, "li.item:first-of-type")

# <input id="user_123_abcd" class="input-field">
# 🎯 Task

# Write:

# Selector using partial ID
# Selector using attribute contains

driver.find_element(By.CSS_SELECTOR, "input[id*='user_']")
driver.find_element(By.CSS_SELECTOR, "input[id^='user_')]")


# <label>Email</label>
# <input type="text" name="email">
# 🎯 Task

# Write:

# Selector for input next to label

driver.find_element(By.CSS_SELECTOR, "label + input")

# <div>
#    <button class="btn">Submit</button>
#    <button class="btn">Cancel</button>
# </div>
# 🎯 Task

# Write:

# Selector for Submit button (CSS only — think carefully 👀)

driver.find_element(By.CSS_SELECTOR, "div > button.btn:first-child")

# <input class="_2IX_2- VJZDxU" type="text" name="username">
# 🎯 Task

# Write:

# Safe selector (avoid dynamic class)
# Attribute-based selector

driver.find_element(By.CSS_SELECTOR, "input[name='username']")
driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='username']")



"""
| XPath         | CSS  |
| ------------- | ---- |
| contains()    | `*=` |
| starts-with() | `^=` |
| ends-with()   | `$=` |
"""