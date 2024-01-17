from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order_page_locators import OrderPageLocators
from constants import Constants
import allure
from faker import Faker


class OrderPageOperations:
    @allure.step('Заполняем поля для успешного заказа')
    def valid_order(self, driver):
        # генерируем произвольную дату в периоде от сегодня до года вперед
        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_TEMPLATE))
        driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(Constants.NAME_FIELD)
        driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(Constants.SURNAME_FIELD)
        driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(Constants.ADDRESS_FIELD)
        driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(OrderPageLocators.METRO_LIST))
        driver.find_element(*OrderPageLocators.CHOOSE_METRO_FIELD).click()
        driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(Constants.PHONE_FIELD)
        driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()
        driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(date)
        driver.find_element(*OrderPageLocators.BLACK_CHECKOX).click()
        driver.find_element(*OrderPageLocators.DURATION_FIELD).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DURATION_LIST))
        driver.find_element(*OrderPageLocators.CHOOSE_DURATION_FIELD).click()
        driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(Constants.СOMMENT)
        driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.CONFIRM_BUTTON))
        driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESS_ORDER))

    @allure.step('Заполняем поля альтернативными данными для успешного заказа')
    def valid_order_alt(self, driver):
        # генерируем произвольную дату в периоде от сегодня до года вперед
        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_TEMPLATE))
        driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(Constants.NAME_FIELD_ALT)
        driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(Constants.SURNAME_FIELD_ALT)
        driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(Constants.ADDRESS_FIELD_ALT)
        driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(OrderPageLocators.METRO_LIST))
        driver.find_element(*OrderPageLocators.CHOOSE_METRO_FIELD_ALT).click()
        driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(Constants.PHONE_FIELD_ALT)
        driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()
        driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(date)
        driver.find_element(*OrderPageLocators.GREY_CHECBOX).click()
        driver.find_element(*OrderPageLocators.CHOOSE_DURATION_FIELD_ALT).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DURATION_LIST))
        driver.find_element(*OrderPageLocators.CHOOSE_DURATION_FIELD_ALT).click()
        driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(Constants.COMMENT_ALT)
        driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.CONFIRM_BUTTON))
        driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESS_ORDER))
