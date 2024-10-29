from selenium.webdriver.common.by import By


class Locators:
    BUTTON_PASS_LINK = (By.XPATH, ".//div/p/a[@href= '/forgot-password']")
    TAG_PASS_REC = (By.XPATH, ".//button[text() = 'Восстановить']")
    CONT_PASS_REC_EMAIL = (By.XPATH, ".//div[@class = 'input__container']//input")
    BUTTON_PASS_REC = (By.XPATH, ".//button[text() = 'Восстановить']")
    BUTTON_PASS_SAVE = (By.XPATH, ".//div/label[text() = 'Введите код из письма']")
    BUTTON_PASS_VIS = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    CONT_PASS_ACTIVE = (By.XPATH, ".//div/div[contains(@class, 'input_status_active')]")
    CONT_LOGIN_EMAIL = (By.XPATH, ".//div/label[text()='Email']/../input")
    CONT_LOGIN_PASS = (By.XPATH, ".//div/label[text()='Пароль']/../input")
    BUTTON_LOGIN = (By.XPATH, ".//button[text() = 'Войти']")
    BUTTON_ACCOUNT = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    BUTTON_ORDER_LIST = (By.XPATH, ".//ul/li/a[text() = 'История заказов']")
    BUTTON_QUIT_PROFILE = (By.XPATH, ".//ul/li/button[text() = 'Выход']")
    LIST_ORDER_HISTORY = (By.XPATH, ".//div/ul[contains(@class, 'OrderHistory')]")
    BUTTON_PLACE_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    TAG_LOGIN = (By.XPATH, ".//div[contains(@class, 'Auth_login')]/h2[text() = 'Вход']")
    TAG_RECOVERY = (By.XPATH, ".//div[contains(@class, 'Auth_login')]/h2[text() = 'Восстановление пароля']")
