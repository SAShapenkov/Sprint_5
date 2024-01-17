from selenium.webdriver.common.by import By

class OrderPageLocators:

 ORDER_TEMPLATE = (By.XPATH, "//*[@class='Order_Form__17u6u']") # Форма заказа
 NAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Имя')]") # Поле Имя
 SURNAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Фамилия')]") # Поле Фамилия
 ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]") # Поле Адрес
 METRO_FIELD = (By.XPATH, "//*[@class='select-search']") # Поле Метро
 DATE_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]") # Поле Дата
 DURATION_FIELD = (By.XPATH, "//*[@class='Dropdown-placeholder']") # Поле Срок аренды
 DURATION_LIST = (By.XPATH, "//*[@class='Dropdown-menu']") # Список вариантов срока аренды
 CHOOSE_DURATION_FIELD = (By.XPATH, ".//div[text()='двое суток']") # Выбор пункта меню
 CHOOSE_DURATION_FIELD_ALT = (By.XPATH, ".//div[text()='сутки']") # Выбор пункта меню дополнительный
 CHOOSE_METRO_FIELD = (By.XPATH, ".//div[text()='Черкизовская']") # Выбор стании метро
 CHOOSE_METRO_FIELD_ALT = (By.XPATH, ".//div[text()='Сокольники']") # Выбор стании метро дополнительный
 METRO_LIST = (By.XPATH, "//*[@class='select-search__select']") # Список станций метро
 PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]") # Поле Телефон
 BLACK_CHECKOX = (By.XPATH, "//*[@id='black']") # Чекбокс для черного цвета
 GREY_CHECBOX = (By.XPATH, "//*[@id='grey']") # Чекбокс для серого цвета
 COMMENT_FIELD = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]") # Поле Комментарий
 BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']") #кнопка Далее
 ORDER_BUTTON = (By.XPATH, ".//button[@class != 'Button_Button__ra12g' and text()='Заказать']") #кнопка Заказать
 CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']") #кнопка Да
 SUCCESS_ORDER = (By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']") # Всплывашка об успешном заказе
