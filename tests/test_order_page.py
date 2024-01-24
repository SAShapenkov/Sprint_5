import allure
from pages.main_page import MainPageOperations
from pages.order_page import OrderPageOperations
from pages.base_page import BasePageOperations
from locators.order_page_locators import OrderPageLocators


class TestOrder:
    @allure.title('Проверка корректного заполнения формы заказа')  # декораторы
    @allure.description(
        'Заходим на главную, переходим в форму заказа, заполняем валидными данными, ожидаем форму успешного заказа')
    def test_bottom_order_button(self, driver):
        order_page = OrderPageOperations(driver)
        main_page = MainPageOperations(driver)
        main_page.open_main_page()
        main_page.scroll_to_button()
        order_page.fill_order_form()
        order_page.fill_rent_form()
        assert 'Заказ оформлен' in order_page.get_confirmation_window_header()
