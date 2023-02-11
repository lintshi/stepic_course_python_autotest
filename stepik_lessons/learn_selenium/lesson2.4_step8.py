import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    priceText = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )

    bookBtn = browser.find_element(By.CSS_SELECTOR, "#book")
    bookBtn.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    y = calc(x.text)

    inputField = browser.find_element(By.CSS_SELECTOR, "#answer")
    inputField.send_keys(y)

    submitBtn = browser.find_element(By.CSS_SELECTOR, "#solve")
    submitBtn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
