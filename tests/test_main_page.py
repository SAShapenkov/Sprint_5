import allure
import pytest
from constants import Constants
from pages.main_page import MainPageOperations
from pages.base_page import BasePageOperations
from locators.main_page_locators import MainPageLocators


class TestMainPage:
    @allure.title('Проверка входа в форму заказа через кнопку снизу')  # декораторы
    @allure.description(
        'На странице ищем кнопку Заказать и проверяем, что происходит корректный переход в форму заказа')
    def test_bottom_order_button(self, driver):
        main_page = MainPageOperations(driver)
        base_page = BasePageOperations(driver)
        main_page.open_main_page()
        main_page.scroll_to_button()
        assert base_page.current_url(driver) == Constants.ORDER_URL


    @allure.title('Проверка соответствия ответам на вопросы')  # декораторы
    @allure.description(
            'На странице ищем блок вопросов, нажимаем на каждый по очереди и проверяем, что текстовка верна')
    @pytest.mark.parametrize(('answers', 'faq_q', 'faq_a'),
        [(Constants.FAQ_T_1, MainPageLocators.FAQ_1_Q, MainPageLocators.FAQ_1_A),
         (Constants.FAQ_T_2, MainPageLocators.FAQ_2_Q, MainPageLocators.FAQ_2_A),
         (Constants.FAQ_T_3, MainPageLocators.FAQ_3_Q, MainPageLocators.FAQ_3_A),
         (Constants.FAQ_T_4, MainPageLocators.FAQ_4_Q, MainPageLocators.FAQ_4_A),
         (Constants.FAQ_T_5, MainPageLocators.FAQ_5_Q, MainPageLocators.FAQ_5_A),
         (Constants.FAQ_T_6, MainPageLocators.FAQ_6_Q, MainPageLocators.FAQ_6_A),
         (Constants.FAQ_T_7, MainPageLocators.FAQ_7_Q, MainPageLocators.FAQ_7_A),
         (Constants.FAQ_T_8, MainPageLocators.FAQ_LAST_Q, MainPageLocators.FAQ_LAST_A)
         ])
    def test_faq_droprown_texts(self, driver, faq_q, faq_a, answers):
        base_page = BasePageOperations(driver)
        main_page = MainPageOperations(driver)
        main_page.open_main_page()
        main_page.scroll_to_bottom()
        base_page.click(faq_q)
        assert base_page.text_extracting(faq_a) == answers
