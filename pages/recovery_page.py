import allure
from pages.base_page import BasePage
from src.data import *
from src.locators import Locators


class RecoveryPass(BasePage):
    @allure.step('Открываем и закрываем браузер Chrome и Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт')
    def login_open(self):
        self.open(URL_LOGIN)

    @allure.step('переход по клику «Восстановить пароль»')
    def click_rec_link(self):
        self.click(Locators.BUTTON_PASS_LINK)

    @allure.step('Ожидание оглавления «Восстановить пароль»')
    def visibility_pass_rec(self):
        self.wait_for_element(Locators.TAG_PASS_REC)

    @allure.step('получение сайта «Восстановить пароль»')
    def get_pass_rec_url(self):
        self.get_current_url()
