import allure
import pytest
from constants import Constants
from pages.main_page import MainPageOperations
from pages.base_page import BasePageOperations
from locators.main_page_locators import MainPageLocators


class TestMainPage(MainPageOperations, BasePageOperations):
    @allure.title('Проверка входа в форму заказа через кнопку снизу')  # декораторы
    @allure.description(
        'На странице ищем кнопку Заказать и проверяем, что происходит корректный переход в форму заказа')
    def test_bottom_order_button(self, driver):
        self.open_main_page(driver)
        self.scroll_to_button(driver)
        current_url = driver.current_url
        assert current_url == Constants.ORDER_URL


    @allure.title('Проверка соответствия ответам на вопросы')  # декораторы
    @allure.description(
            'На странице ищем блок вопросов, нажимаем на каждый по очереди и проверяем, что текстовка верна')
    @pytest.mark.parametrize(('answers', 'faq_q', 'faq_a'),
        [('Сутки — 400 рублей. Оплата курьеру — наличными или картой.', MainPageLocators.FAQ_1_Q, MainPageLocators.FAQ_1_A),
         ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.', MainPageLocators.FAQ_2_Q, MainPageLocators.FAQ_2_A),
         ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', MainPageLocators.FAQ_3_Q, MainPageLocators.FAQ_3_A),
         ('Только начиная с завтрашнего дня. Но скоро станем расторопнее.', MainPageLocators.FAQ_4_Q, MainPageLocators.FAQ_4_A),
         ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', MainPageLocators.FAQ_5_Q, MainPageLocators.FAQ_5_A),
         ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.', MainPageLocators.FAQ_6_Q, MainPageLocators.FAQ_6_A),
         ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', MainPageLocators.FAQ_7_Q, MainPageLocators.FAQ_7_A),
         ('Да, обязательно. Всем самокатов! И Москве, и Московской области.', MainPageLocators.FAQ_LAST_Q, MainPageLocators.FAQ_LAST_A)
         ])
    def test_faq_droprown_texts(self, driver, faq_q, faq_a, answers):
        self.open_main_page(driver)
        self.scroll_to_bottom(driver)
        self.click(driver, faq_q)
        element_text = driver.find_element(*faq_a).text
        assert element_text == answers
