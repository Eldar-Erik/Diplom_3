from selenium.webdriver.common.by import By


class Locators:
    BUTTON_PASS_LINK = (By.XPATH, ".//div/p/a[@href= '/forgot-password']")
    TAG_PASS_REC = (By.XPATH, ".//button[text() = 'Восстановить']")
    CONT_PASS_REC_EMAIL = (By.XPATH, ".//div[@class = 'input__container']//input")
    BUTTON_PASS_REC = (By.XPATH, ".//button[text() = 'Восстановить']")
    BUTTON_PASS_SAVE = (By.XPATH, ".//div/label[text() = 'Введите код из письма']")
    BUTTON_PASS_VIS = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    CONT_PASS_ACTIVE = (By.XPATH, ".//div/div[contains(@class, 'input_status_active')]")