from selenium.webdriver.common.by import By


class Locators:
    BUTTON_PASS_LINK = (By.XPATH, ".//div/p/a[@href= '/forgot-password']")
    TAG_PASS_REC = (By.XPATH, ".//button[text() = 'Восстановить']")
