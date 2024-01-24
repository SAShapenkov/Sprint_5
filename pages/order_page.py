from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePageOperations
from constants import Constants
import allure
from faker import Faker


class OrderPageOperations(BasePageOperations):

    @allure.step('Заполняем поля для успешного заказа')
    def valid_order(self):
        # генерируем произвольную дату в периоде от сегодня до года вперед
        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")

        self.wait_for_visibility(OrderPageLocators.ORDER_TEMPLATE)
        self.send_data_to_locator(OrderPageLocators.NAME_FIELD, Constants.NAME_FIELD)
        self.send_data_to_locator(OrderPageLocators.SURNAME_FIELD, Constants.SURNAME_FIELD)
        self.send_data_to_locator(OrderPageLocators.ADDRESS_FIELD, Constants.ADDRESS_FIELD)
        self.click(OrderPageLocators.METRO_FIELD)
        self.wait_for_visibility(OrderPageLocators.METRO_LIST)
        self.click(OrderPageLocators.CHOOSE_METRO_FIELD)
        self.send_data_to_locator(OrderPageLocators.PHONE_FIELD, Constants.PHONE_FIELD)
        self.click(OrderPageLocators.BUTTON_NEXT)
        self.send_data_to_locator(OrderPageLocators.DATE_FIELD, date)
        self.click(OrderPageLocators.BLACK_CHECKOX)
        self.click(OrderPageLocators.DURATION_FIELD)
        self.wait_for_visibility(OrderPageLocators.DURATION_LIST)
        self.click(OrderPageLocators.CHOOSE_DURATION_FIELD)
        self.send_data_to_locator(OrderPageLocators.COMMENT_FIELD, Constants.СOMMENT)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_visibility(OrderPageLocators.CONFIRM_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)
        self.wait_for_visibility(OrderPageLocators.SUCCESS_ORDER)

    @allure.step('Заполняем поля альтернативными данными для успешного заказа')
    def valid_order_alt(self, driver):
        # генерируем произвольную дату в периоде от сегодня до года вперед
        faker = Faker()
        fake_date = faker.date_between(start_date='today', end_date='+1y')
        date = fake_date.strftime("%Y-%m-%d")


        self.wait_for_visibility(OrderPageLocators.ORDER_TEMPLATE)
        self.send_data_to_locator(OrderPageLocators.NAME_FIELD, Constants.NAME_FIELD_ALT)
        self.send_data_to_locator(OrderPageLocators.SURNAME_FIELD, Constants.SURNAME_FIELD_ALT)
        self.send_data_to_locator(OrderPageLocators.ADDRESS_FIELD, Constants.ADDRESS_FIELD_ALT)
        self.click(OrderPageLocators.METRO_FIELD)
        self.wait_for_visibility(OrderPageLocators.METRO_LIST)
        self.click(OrderPageLocators.CHOOSE_METRO_FIELD_ALT)
        self.send_data_to_locator(OrderPageLocators.PHONE_FIELD, Constants.PHONE_FIELD_ALT)
        self.click(OrderPageLocators.BUTTON_NEXT)
        self.send_data_to_locator(OrderPageLocators.DATE_FIELD, date)
        self.click(OrderPageLocators.GREY_CHECBOX)
        self.click(OrderPageLocators.DURATION_FIELD)
        self.wait_for_visibility(OrderPageLocators.DURATION_LIST)
        self.click(OrderPageLocators.CHOOSE_DURATION_FIELD_ALT)
        self.send_data_to_locator(OrderPageLocators.COMMENT_FIELD, Constants.COMMENT_ALT)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_visibility(OrderPageLocators.CONFIRM_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)
        self.wait_for_visibility(OrderPageLocators.SUCCESS_ORDER)

