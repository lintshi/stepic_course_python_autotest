import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answerInput = browser.find_element(By.CSS_SELECTOR, "#answer")
    answerInput.send_keys(y)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robotsRule.click()

    submitBtn = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
