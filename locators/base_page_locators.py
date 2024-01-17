from selenium.webdriver.common.by import By

class NavBar:

 SAMOKAT_LOGO = (By.XPATH, "//*[@class='Header_LogoScooter__3lsAR']") # Кнопка Самокат
 YA_LOGO = (By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']") # Кнопка Яндекс
 ORDER_BUTTON = (By.XPATH, "//*[@class='Button_Button__ra12g']") # Кнопка Заказать
 ORDER_STATUS_BUTTON = (By.XPATH, "//*[@class='Header_Link__1TAG7']")  # Кнопка Статус заказа
 DZEN_LOGO = (By.XPATH, "//*[@class='desktop-base-header__logoLink-aE']") #Лого Дзен