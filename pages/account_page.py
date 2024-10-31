import allure
from pages.base_page import BasePage
from src.data import *
from src.locators import Locators


class AccountPage(BasePage):
    @allure.step('Открываем и закрываем браузер Chrome и Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт "Login"')
    def login_open(self):
        self.open(URL_LOGIN)

    @allure.step('Ввод email в поле логина')
    def enter_login(self):
        self.send_keys(Locators.CONT_LOGIN_EMAIL, LOG_EMAIL)

    @allure.step('Ввод password в поле пароля')
    def enter_pass(self):
        self.send_keys(Locators.CONT_LOGIN_PASS, PAS)

    @allure.step('Нажать кнопку авторизации')
    def login_button_click(self):
        self.click(Locators.BUTTON_LOGIN)

    @allure.step('Ожидание перехода на домашнюю страницу')
    def wait_for_home(self):
        self.wait_for_element(Locators.BUTTON_PLACE_ORDER)

    @allure.step('Обьеденить шаг входа в профиль')
    def login_enter(self):
        self.enter_login()
        self.enter_pass()
        self.login_button_click()
        self.wait_for_home()

    @allure.step('Нажать кнопку Личный кабинет')
    def account_button_click(self):
        self.click(Locators.BUTTON_ACCOUNT)

    @allure.step('Ожидание загрузки профиля')
    def wait_for_profile_site(self):
        return self.wait_for_element(Locators.BUTTON_QUIT_PROFILE)

    def history_button_click(self):
        self.click(Locators.BUTTON_ORDER_HISTORY)

    @allure.step('Ожидание загрузки списка заказов')
    def wait_for_history_list(self):
        return self.wait_for_element(Locators.LIST_ORDER_HISTORY)

    @allure.step('Нажать кнопку выход')
    def click_quit_button(self):
        self.click(Locators.BUTTON_QUIT_PROFILE)

    @allure.step('Проверка страницы входа')
    def get_login_page(self):
        return self.wait_for_element(Locators.TAG_LOGIN)
