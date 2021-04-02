from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    sumnum=int(num1)+int(num2)
    sumstr=str(sumnum)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{sumstr}']").click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()