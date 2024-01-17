import allure
from constants import Constants
from pages.main_page import MainPageOperations
from pages.base_page import BasePageOperations


class TestBasePage(BasePageOperations,MainPageOperations):

    @allure.title('Проверка входа в форму заказа через кнопку сверху')  # декораторы
    @allure.description(
        'На странице в шапке ищем кнопку Заказать и проверяем, что происходит корректный переход в форму заказа')
    def test_upper_order_button(self, driver):
        self.open_main_page(driver)
        self.order_button_click(driver)
        current_url = driver.current_url
        assert current_url == Constants.ORDER_URL

    @allure.title('Проверка возврата на главную страницу при нажатии лого Самокат')  # декораторы
    @allure.description(
        'Переходим в форму заказа, нажимаем на лого Самокат, проверяем корректность перехода на главную')
    def test_redirect_to_main_from_order(self, driver):
        self.open_main_page(driver)
        self.order_button_click(driver)
        self.samokat_logo_click(driver)
        current_url = driver.current_url
        assert current_url == Constants.MAIN_URL

    @allure.title('Проверка возврата на главную страницу при нажатии лого Самокат')  # декораторы
    @allure.description(
        'Переходим в форму заказа, нажимаем на лого Самокат, проверяем корректность перехода на гавную')
    def test_redirect_to_dzen_from_order(self, driver):
        self.open_main_page(driver)
        self.logo_to_dzen(driver)
        current_url = driver.current_url
        current_url = current_url.partition('/?y')[0]
        assert current_url == Constants.DZEN_URL
