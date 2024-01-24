import allure
from constants import Constants
from pages.main_page import MainPageOperations
from pages.base_page import BasePageOperations



class TestBasePage:

    @allure.title('Проверка входа в форму заказа через кнопку сверху')  # декораторы
    @allure.description(
        'На странице в шапке ищем кнопку Заказать и проверяем, что происходит корректный переход в форму заказа')
    def test_upper_order_button(self, driver):
        main_page = MainPageOperations(driver)
        base_page = BasePageOperations(driver)
        base_page.open_main_page()
        main_page.order_button_click()
        assert base_page.current_url(driver) == Constants.ORDER_URL

    @allure.title('Проверка возврата на главную страницу при нажатии лого Самокат')  # декораторы
    @allure.description(
        'Переходим в форму заказа, нажимаем на лого Самокат, проверяем корректность перехода на главную')
    def test_redirect_to_main_from_order(self, driver):
        main_page = MainPageOperations(driver)
        base_page = BasePageOperations(driver)
        base_page.open_main_page()
        main_page.order_button_click()
        main_page.samokat_logo_click()
        assert base_page.current_url(driver) == Constants.MAIN_URL

    @allure.title('Проверка возврата на главную страницу при нажатии лого Самокат')  # декораторы
    @allure.description(
        'Переходим в форму заказа, нажимаем на лого Самокат, проверяем корректность перехода на гавную')
    def test_redirect_to_dzen_from_order(self, driver):
        main_page = MainPageOperations(driver)
        base_page = BasePageOperations(driver)
        base_page.open_main_page()
        main_page.logo_to_dzen()
        assert base_page.url_partition(driver) == Constants.DZEN_URL
