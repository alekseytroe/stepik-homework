# Задание: ждем нужный текст на странице
#
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.
#
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
#     +Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#     +Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#     +Нажать на кнопку "Book"
#     +Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
#
# Чтобы определить момент, когда цена аренды уменьшится до $100,
# используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
#
# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button = browser.find_element_by_id('book')
    button.click()

#   промотать страницу вниз до элемента id="input_value"
    input_value = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)
    input_number = int(input_value.text)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(input_number))

    # отправить решение
    solve_button = browser.find_element_by_id('solve')
    solve_button.click()

finally:
    time.sleep(10)
    browser.quit()

