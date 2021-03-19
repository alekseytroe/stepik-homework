# 1. +Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
# 2. +Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
# 3. +Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен
#       объявляться в фикстуре browser и передаваться в тест как параметр.
# 4. +В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку
#       добавления в корзину. Например, можно проверять товар, доступный по
#       http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
# 5. +Тест должен запускаться с параметром language следующей командой:
#       pytest --language=es test_items.py #
#       и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

import time

# страница с корзиной
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# страница без корзины
# link = 'https://stepik.org/'


def test_should_be_basket_btn(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements_by_css_selector('button.btn-add-to-basket'), 'Нет кнопки добавления в корзину!'

