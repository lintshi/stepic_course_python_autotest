import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstNumber = browser.find_element(By.CSS_SELECTOR, "#num1")
    secondNumber = browser.find_element(By.CSS_SELECTOR, "#num2")

    sum = int(firstNumber.text) + int(secondNumber.text)

    dropDown = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    dropDown.select_by_value(str(sum))

    submitBtn = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitBtn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
