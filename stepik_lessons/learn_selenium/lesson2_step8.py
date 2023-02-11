import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.CSS_SELECTOR, "[name = \"firstname\"]")
    firstName.send_keys("Ive")

    lastName = browser.find_element(By.CSS_SELECTOR, "[name = \"lastname\"]")
    lastName.send_keys("Johnes")

    email = browser.find_element(By.CSS_SELECTOR, "[name = \"email\"]")
    email.send_keys("ive@johnes.to")

    loadFile = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    loadFile.send_keys(file_path)

    submitBtn = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitBtn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
