import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import math

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_does_item_have_add_to_cart_button(browser):

    # На всякий случай
    browser.implicitly_wait(10)

    # Открыть страницу товара
    browser.get(link)

    # Пауза чтобы проверить текст в кнопке
    time.sleep(10)

    # Найти кнопку добавления в карзину с помощью elements, который возвращает массив
    # (будет пустой массив если элементы не были найдены)
    add_to_cart_button = browser.find_elements(
        By.CSS_SELECTOR, 'button.btn-add-to-basket')

    # Проверить найдена ли кнопка
    assert len(
        add_to_cart_button) is not 0, 'Кнопка добавления в карзину не найдена'

    pass
