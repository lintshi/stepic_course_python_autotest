import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSelectors(unittest.TestCase):
    def testOne(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        firstName = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        firstName.send_keys("Ivan")

        lastName = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        lastName.send_keys("Ivanov")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        email.send_keys("ivan@ivan.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        browser.quit()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test One failed")

    def testTwo(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        firstName = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        firstName.send_keys("Ivan")

        lastName = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        lastName.send_keys("Ivanov")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        email.send_keys("ivan@ivan.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        browser.quit()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test One failed")

if __name__ == "__main__":
        unittest.main()
