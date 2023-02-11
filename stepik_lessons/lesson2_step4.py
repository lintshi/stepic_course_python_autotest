import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    magicBtn = browser.find_element(By.CSS_SELECTOR, ".btn")
    magicBtn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)
    inputField = browser.find_element(By.CSS_SELECTOR, "#answer")
    inputField.send_keys(y)

    submitBtn = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitBtn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
