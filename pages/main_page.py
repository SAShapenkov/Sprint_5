from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePageOperations
from locators.base_page_locators import NavBar
import allure


class MainPageOperations(BasePageOperations):

    @allure.step('Открываем браузер Firefox, заходим на страницу Самокатов')
    def open_main_page(self):
        self.wait_for_visibility(MainPageLocators.SCOOTER_BLUEPRINT_IMAGE)

    @allure.step('Нажимаем на лого Яндекс')
    def ya_logo_click(self):
        self.click(NavBar.YA_LOGO)

    @allure.step('Нажимаем на лого Самокат')
    def samokat_logo_click(self):
        self.click(NavBar.SAMOKAT_LOGO)

    @allure.step('Нажимаем на кнопку Заказать (верхнее статичное меню)')
    def order_button_click(self):
        self.click(NavBar.ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку Статус заказа')
    def order_status_button_click(self):
        self.click(NavBar.ORDER_STATUS_BUTTON)

    @allure.step('Жмем лого ЯНдекс, переключаемся на вкладку, ждем пока загрузит лого')
    def logo_to_dzen(self):
        self.ya_logo_click()
        self.switch_to_window()
        self.wait_for_visibility(NavBar.DZEN_LOGO)

    @allure.step('Выполняем скролл до последнего вопроса')
    def scroll_to_bottom(self):
        self.scroll_to_element(MainPageLocators.FAQ_LAST_Q)
        self.wait_for_visibility(MainPageLocators.FAQ_LAST_Q)

    @allure.step('Скроллим и нажимаем на кнопку Заказать на главной странице')
    def scroll_to_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MP)
        self.wait_for_click_available(MainPageLocators.ORDER_BUTTON_MP)
        self.click(MainPageLocators.ORDER_BUTTON_MP)
        self.wait_for_click_available(OrderPageLocators.ORDER_TEMPLATE)


