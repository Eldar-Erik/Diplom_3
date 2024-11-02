import allure
from pages.base_page import BasePage
from src.data import *
from src.locators import Locators
from src.helpers import random_reg_email


class RecoveryPass(BasePage):
    @allure.step('Открываем и закрываем браузер Chrome и Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт "Login"')
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

    @allure.step('Открываем сайт "Recovery"')
    def rec_open(self):
        self.open(URL_PASS_REC)

    @allure.step('Вписывает email')
    def send_email(self):
        self.send_keys(Locators.CONT_PASS_REC_EMAIL, random_reg_email())

    @allure.step('Вписывает email')
    def press_rec_button(self):
        self.click(Locators.BUTTON_PASS_REC)

    @allure.step('Проверка наличия кнопки "Сохранить"')
    def get_save_button(self):
        return self.wait_for_element(Locators.BUTTON_PASS_SAVE)

    @allure.step('Нажать на кнопку видимости пароля')
    def press_vis_button(self):
        self.click(Locators.BUTTON_PASS_VIS)

    @allure.step('Вилимость активного окна пароля')
    def get_active_cont(self):
        return self.wait_for_element(Locators.CONT_PASS_ACTIVE)
