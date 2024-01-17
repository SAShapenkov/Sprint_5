import allure
from pages.main_page import MainPageOperations
from pages.base_page import BasePageOperations
from pages.order_page import OrderPageOperations
from locators.order_page_locators import OrderPageLocators


class TestOrder(MainPageOperations, BasePageOperations, OrderPageOperations):
    @allure.title('Проверка корректного заполнения формы заказа')  # декораторы
    @allure.description(
        'Заходим на главную, переходим в форму заказа, заполняем валидными данными, ожидаем форму успешного заказа')
    def test_bottom_order_button(self, driver):
        self.open_main_page(driver)
        self.scroll_to_button(driver)
        self.valid_order(driver)
        assert  driver.find_element(*OrderPageLocators.SUCCESS_ORDER)
