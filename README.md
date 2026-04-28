# Web Locator Strategies for Automation Testing

## 📌 Project Overview

This project demonstrates **web locator strategies** used in UI automation testing. Locator strategies are essential for identifying and interacting with elements on a web page using tools like Selenium.

The goal of this project is to provide:

* Clear understanding of different locator types
* Practical examples using real-world DOM structures
* Best practices for writing stable and maintainable locators

---

## 🛠️ Technologies Used

* Python
* Selenium WebDriver
* Chrome Browser
* HTML (for DOM understanding)

---

## 🔍 Locator Strategies Covered

### 1. ID Locator

* Uses the `id` attribute
* Fastest and most reliable

```python
driver.find_element(By.ID, "username")
```

---

### 2. Name Locator

* Uses the `name` attribute

```python
driver.find_element(By.NAME, "email")
```

---

### 3. Class Name Locator

* Uses a single class value

```python
driver.find_element(By.CLASS_NAME, "login-btn")
```

⚠️ Note: Cannot use multiple classes together

---

### 4. Tag Name Locator

* Uses HTML tag

```python
driver.find_element(By.TAG_NAME, "input")
```

---

### 5. Link Text Locator

* Matches exact text of links

```python
driver.find_element(By.LINK_TEXT, "Login")
```

---

### 6. Partial Link Text Locator

* Matches partial text

```python
driver.find_element(By.PARTIAL_LINK_TEXT, "Log")
```

---

### 7. CSS Selector (Recommended)

* Flexible and fast
* Supports ID, class, attributes, hierarchy

#### Examples:

```python
# ID
driver.find_element(By.CSS_SELECTOR, "#username")

# Class
driver.find_element(By.CSS_SELECTOR, ".login-btn")

# Multiple classes
driver.find_element(By.CSS_SELECTOR, ".btn.primary.login-btn")

# Attribute
driver.find_element(By.CSS_SELECTOR, "input[name='email']")

# Partial match
driver.find_element(By.CSS_SELECTOR, "input[id*='user_']")

# Child
driver.find_element(By.CSS_SELECTOR, "div.form > input")

# Descendant
driver.find_element(By.CSS_SELECTOR, "div.form input")
```

---

### 8. XPath Locator

* Most powerful and flexible
* Can navigate DOM structure

```python
driver.find_element(By.XPATH, "//input[@id='username']")
driver.find_element(By.XPATH, "//button[text()='Login']")
```

#### Advanced XPath:

```python
//input[contains(@id,'user')]
//button[starts-with(@class,'btn')]
```

---

## 🧪 Example Automation Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()
```

---

## 📚 Learning Outcomes

By completing this project, I understand:

* All locator strategies
* Write efficient and stable selectors
* Handle dynamic web elements
* Improve real-world automation skills

---

## 🚀 Future Improvements

* Add real website automation examples
* Integrate with PyTest framework
* Include explicit waits (WebDriverWait)
* Build end-to-end test scenarios

---

## 📌 Conclusion

Locator strategies are the backbone of automation testing. Mastering them ensures:

* Stable test scripts
* Reduced maintenance effort
* Better performance in test execution

---
