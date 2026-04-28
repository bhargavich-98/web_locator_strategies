# <input type="text" id="twotabsearchtextbox" name="field-keywords" class="nav-input">



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.find_element(By.ID, "twotabsearchtextbox")
driver.find_element(By.NAME, "field-keywords")
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")


# search button
# <input type="submit" id="nav-search-submit-button" class="nav-input nav-progressive-attribute">
driver.find_element(By.ID, "nav-search-submit-button")
driver.find_element(By.CSS_SELECTOR, "input#nav-search-submit-button")
driver.find_element(By.XPATH, "//input[@type='submit']")

# product title
# <span class="a-size-medium a-color-base a-text-normal">Apple iPhone 14 (128 GB)</span>

driver.find_element(By.CLASS_NAME, "a-size-medium")
driver.find_element(By.CSS_SELECTOR, "span.a-size-medium.a-color-base")
driver.find_element(By.XPATH, "//span[contains(text(), 'iphone')]")

# <input type="text" class="Pke_EE" name="q" placeholder="Search for products">
driver.find_element(By.NAME, "q")
driver.find_element(By.CSS_SELECTOR, "input[name='q']")
driver.find_element(By.XPATH, "//input[@name='q']")

#<button class="_2KpZ6l _2doB4z">✕</button>
driver.find_element(By.XPATH, "//button[text()='✕']")
driver.find_element(By.XPATH, "//button[contains(@class, '_2KpZ6l')]")

# <a class="IRpwTa" href="/apple-iphone-14/p/itm123">Apple iPhone 14</a>
driver.find_element(By.LINK_TEXT, "Apple iPhone 14")
driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone")
driver.find_element(By.XPATH, "//a[contains(text(), 'iPhone')]")