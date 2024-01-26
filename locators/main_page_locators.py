from selenium.webdriver.common.by import By
class MainPageLocators:
    SCOOTER_FIELD = (By.XPATH, "//*[@class='Home_Scooter__3YdJy']")  # Поле с самокатом
    SCOOTER_BLUEPRINT_IMAGE = (By.XPATH, "//*[@class='Home_BluePrint__TGX2n']")  # Поле с чертежом самоката
    FAQ_1_Q = (By.ID, "accordion__heading-0")  # Первый пункт вопросов
    FAQ_2_Q = (By.ID, "accordion__heading-1")  # Второй пункт вопросов
    FAQ_3_Q = (By.ID, "accordion__heading-2")  # Третий пункт вопросов
    FAQ_4_Q = (By.ID, "accordion__heading-3")  # Четвертый пункт вопросов
    FAQ_5_Q = (By.ID, "accordion__heading-4")  # Пятый пункт вопросов
    FAQ_6_Q = (By.ID, "accordion__heading-5")  # Шестой пункт вопросов
    FAQ_7_Q = (By.ID, "accordion__heading-6")  # Седьмой пункт вопросов
    FAQ_LAST_Q = (By.ID, "accordion__heading-7")  # Последний пункт вопросов
    FAQ_1_A = (By.ID, "accordion__panel-0")  # Ответ на первый вопрос
    FAQ_2_A = (By.ID, "accordion__panel-1")  # Ответ на второй вопрос
    FAQ_3_A = (By.ID, "accordion__panel-2")  # Ответ на третий вопрос
    FAQ_4_A = (By.ID, "accordion__panel-3")  # Ответ на четвертый вопрос
    FAQ_5_A = (By.ID, "accordion__panel-4")  # Ответ на пятый вопрос
    FAQ_6_A = (By.ID, "accordion__panel-5")  # Ответ на шестой вопрос
    FAQ_7_A = (By.ID, "accordion__panel-6")  # Ответ на седьмой вопрос
    FAQ_LAST_A = (By.ID, "accordion__panel-7")  # Ответ на последний вопрос
    ORDER_BUTTON_MP = (By.XPATH, "//*[@class='Home_FinishButton__1_cWm']")  # Кнопка Заказать на главной странице