import allure
from pages.base_page import BasePage
from src.data import *
from src.locators import Locators


class HomePage(BasePage):

    @allure.step('Открываем и закрываем браузер Chrome и Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем сайт "Login"')
    def login_open(self):
        self.open(URL_LOGIN)

    @allure.step('Открываем сайт "Home"')
    def home_open(self):
        self.open(URL_HOME)

    @allure.step('Нажимаем на кнопку конструктор')
    def click_constructor_button(self):
        self.click(Locators.BUTTON_CONSTRUCTOR)

    @allure.step('Ждём загрузку оглавления конструктора')
    def wait_constructor_site(self):
        return self.wait_for_element(Locators.TAG_CONSTRUCTOR)

    @allure.step('Поиск конструктора')
    def vis_constructor_site(self):
        return self.wait_for_element(Locators.LIST_CONSTRUCTOR)

    @allure.step('Жмём кнопку лента заказов')
    def click_order_list_button(self):
        self.click(Locators.BUTTON_ORDER_LIST)

    @allure.step('Ожидание загрузки Листа заказов')
    def wait_for_order_list(self):
        return self.wait_for_element(Locators.LIST_ORDER_LIST)

    @allure.step('Проверка Оглавления')
    def get_order_list_toc(self):
        return self.is_element_visible(Locators.TAG_ORDER_LIST)

    @allure.step('нажимаем на ингридиент')
    def click_on_ingredient(self):
        self.click(Locators.BUTTON_INGREDIENT)

    @allure.step('Ожидание загрузки всплывающего окна')
    def wait_for_ingredient_window(self):
        return self.wait_for_element(Locators.WINDOW_INGREDIENT)

    @allure.step('Проверка видимости заголовка всплывающего окна')
    def vis_toc(self):
        return self.is_element_visible(Locators.TAG_WINDOW_INGREDIENT)

    @allure.step('Закрытие всплывающего окна ингридиентов')
    def close_ingredient_window(self):
        self.click(Locators.BUTTON_QUIT_ING_WINDOW)

    @allure.step('перетягиваем ингридиент в корзину')
    def action_ingridient(self):
        self.action_chain(Locators.BUTTON_INGREDIENT, Locators.CONT_BURGER_BASKET)

    @allure.step('проверям текст счетчика')
    def get_ingredient_counter(self):
        return self.get_text(Locators.TAG_INGREDIENT_COUNTER)

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

    @allure.step('нажать кнопку "оформить заказ"')
    def click_order_button(self):
        self.click(Locators.BUTTON_ORDER)

    @allure.step('получаем маяк заказа')
    def get_order_success(self):
        return self.wait_for_element(Locators.TAG_ORDER_SUCCESS)
