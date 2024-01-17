from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import NavBar
import allure

class BasePageOperations:
    @allure.step('Нажимаем на лого Яндекс')
    def ya_logo_click(self, driver):
        driver.find_element(*NavBar.YA_LOGO).click()

    @allure.step('Нажимаем на лого Самокат')
    def samokat_logo_click(self, driver):
        driver.find_element(*NavBar.SAMOKAT_LOGO).click()

    @allure.step('Нажимаем на кнопку Заказать (верхнее статичное меню)')
    def order_button_click(self, driver):
        driver.find_element(*NavBar.ORDER_BUTTON).click()

    @allure.step('Нажимаем на кнопку Статус заказа')
    def order_status_button_click(self, driver):
        driver.find_element(*NavBar.ORDER_STATUS_BUTTON).click()

    @allure.step('Жмем лого ЯНдекс, переключаемся на вкладку, ждем пока загрузит лого')
    def logo_to_dzen(self, driver):
        self.ya_logo_click(driver)
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(NavBar.DZEN_LOGO))

    def click(self, driver, locator):
        driver.find_element(*locator).click()
