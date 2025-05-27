from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # открыть ссылку
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #  Дождаться, когда цена дома уменьшится до $100
    button = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    browser.find_element(By.ID, "book").click()

    # находим x и вычисляем y
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    x = calc(x)

    # вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(x)

    # нажимаем Submit
    browser.find_element(By.ID, "solve").click()

finally:
    # чтобы успеть увидеть результат
    time.sleep(30)
    browser.quit()


