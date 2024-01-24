from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePageOperations:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание появления элемента')
    def wait_for_visibility(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание возможности нажатия на элемент')
    def wait_for_click_available(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
    @allure.step('Поиск элемента')
    def search_for_element(self, locator):
        self.driver.find_element(*locator)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скроллим страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Получаем текущий URL')
    def current_url(self, driver):
        current_url = driver.current_url
        return current_url

    @allure.step('Получаем текущий URL без лишних параметров')
    def url_partition(self, driver):
        current_url = driver.current_url
        current_url = current_url.partition('/?y')[0]
        return current_url

    def text_extracting(self, text):
        element_text = self.driver.find_element(*text).text
        return element_text


    def send_data_to_locator(self, locator, info):
        self.driver.find_element(*locator).send_keys(info)

    @allure.step('Переключиться на новую вкладку')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
