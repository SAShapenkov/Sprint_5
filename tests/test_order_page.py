import allure
from pages.main_page import MainPageOperations
from pages.order_page import OrderPageOperations
from locators.order_page_locators import OrderPageLocators


class TestOrder:
    @allure.title('Проверка корректного заполнения формы заказа')  # декораторы
    @allure.description(
        'Заходим на главную, переходим в форму заказа, заполняем валидными данными, ожидаем форму успешного заказа')
    def test_bottom_order_button(self, driver):
        order_page = OrderPageOperations(driver)
        main_page = MainPageOperations(driver)
        order_loc = OrderPageLocators()
        main_page.open_main_page()
        main_page.scroll_to_button()
        order_page.valid_order()
        assert driver.find_element(*order_loc.SUCCESS_ORDER)
