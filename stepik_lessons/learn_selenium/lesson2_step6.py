import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)
    inputField = browser.find_element(By.CSS_SELECTOR, "#answer")
    inputField.send_keys(y)


    submitBtn = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitBtn)

    checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkBox.click()

    radioBtn = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radioBtn.click()

    submitBtn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
