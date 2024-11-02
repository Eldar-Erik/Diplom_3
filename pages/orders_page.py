import allure
from pages.base_page import BasePage
from src.data import *
from src.locators import Locators
import time


class OrderPage(BasePage):
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
        return self.wait_for_element(Locators.BUTTON_PLACE_ORDER)

    @allure.step('Обьеденить шаг входа в профиль')
    def login_enter(self):
        self.enter_login()
        self.enter_pass()
        self.login_button_click()
        self.wait_for_home()

    @allure.step('Жмём кнопку лента заказов')
    def click_order_list_button(self):
        self.click(Locators.BUTTON_ORDER_LIST)

    @allure.step('Нажимаем на заказ')
    def clico_order_cont(self):
        self.click(Locators.CONT_ORDER_LIST)

    @allure.step('Ждём открытия окна')
    def wait_for_window(self):
        return self.wait_for_element(Locators.WINDOW_ORDER)

    @allure.step('Проверяем тэг окна')
    def vis_tag_window(self):
        return self.is_element_visible(Locators.TAG_ORDER_WINDOW)

    @allure.step('перетягиваем ингридиент в корзину')
    def action_ingridient(self):
        self.action_chain(Locators.BUTTON_INGREDIENT, Locators.CONT_BURGER_BASKET)

    @allure.step('нажать кнопку "оформить заказ"')
    def click_order_button(self):
        self.click(Locators.BUTTON_ORDER)

    @allure.step('Ждем номер заказа')
    def wait_order_prepare(self):
        self.wait_for_element(Locators.TAG_ORDER_PREPARE)

    @allure.step('Закрываем окно заказа')
    def close_order_prepare_window(self):
        self.click(Locators.BUTTON_QUIT_ORDER_WINDOW)

    @allure.step('Нажать кнопку Личный кабинет')
    def account_button_click(self):
        self.click(Locators.BUTTON_ACCOUNT)

    @allure.step('Нажать кнопку "История заказов"')
    def history_button_click(self):
        self.click(Locators.BUTTON_ORDER_HISTORY)

    @allure.step('Ожидание загрузки списка заказов')
    def wait_for_history_list(self):
        return self.wait_for_element(Locators.LIST_ORDER_HISTORY)

    def scroll_down_order_list(self):
        self.scroll_down(Locators.TAG_ORDER_HISTORY_NUMBER)

    @allure.step('Получаем номер последнего заказа в истории')
    def get_order_from_history(self):
        return self.get_text(Locators.TAG_ORDER_HISTORY_NUMBER)

    @allure.step('Жмём кнопку лента заказов')
    def click_order_list_button(self):
        self.click(Locators.BUTTON_ORDER_LIST)

    @allure.step('Получаем номер первого заказа в листе')
    def get_order_from_list(self):
        return self.get_text(Locators.TAG_ORDER_LIST_NUMBER)

    @allure.step('Получаем количество заказов в истории')
    def get_orders_from_list(self):
        return self.get_text(Locators.TAG_ORDERS_COUNTER)

    @allure.step('Нажимаем на кнопку конструктор')
    def click_constructor_button(self):
        self.click(Locators.BUTTON_CONSTRUCTOR)

    @allure.step('Ждём загрузку оглавления конструктора')
    def wait_constructor_site(self):
        return self.wait_for_element(Locators.TAG_CONSTRUCTOR)

    @allure.step('Поиск конструктора')
    def vis_constructor_site(self):
        return self.wait_for_element(Locators.LIST_CONSTRUCTOR)

    @allure.step('Получаем количество сегодняшних заказов в истории')
    def get_today_orders_from_list(self):
        return self.get_text(Locators.TAG_TODAY_ORDERS_COUNTER)

    @allure.step('Получаем номер заказа при оформлении')
    def get_order_numer_by_order(self):
        return self.get_text(Locators.TAG_ORDER_PREPARE)

    @allure.step('Ждём появления носера в работе')
    def wait_for_numer_in_work(self):
        time.sleep(5)

    @allure.step('Получаем номер заказа в работе')
    def get_order_numer_in_work(self):
        return self.get_text(Locators.TAG_ORDER_LIST_PREPARE)
