from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()