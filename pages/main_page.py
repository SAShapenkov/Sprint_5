from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import pytest

import allure
from faker import Faker

class MainPageOperations:
    @allure.step('Открываем браузер Firefox, заходим на страницу Самокатов')
    def open_main_page(self, driver):
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SCOOTER_BLUEPRINT_IMAGE))

    @allure.step('Выполняем скролл до последнего вопроса')
    def scroll_to_bottom(self, driver):
        element = driver.find_element(*MainPageLocators.FAQ_LAST_Q)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.FAQ_LAST_Q))

    @allure.step('Скроллим и нажимаем на кнопку Заказать на главной странице')
    def scroll_to_button(self, driver):
        element = driver.find_element(*MainPageLocators.ORDER_BUTTON_MP)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_MP))
        driver.find_element(*MainPageLocators.ORDER_BUTTON_MP).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.ORDER_TEMPLATE))
