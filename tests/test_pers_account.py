import allure
from pages.account_page import AccountPage


class TestAccountPage:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_personal_account_button_click_success(self, driver):
        acc = AccountPage(driver)
        acc.login_open()
        acc.login_enter()
        acc.account_button_click()
        assert acc.wait_for_profile_site()

    @allure.title('Переход в раздел «История заказов»')
    def test_order_list_success(self, driver):
        acc = AccountPage(driver)
        acc.login_open()
        acc.login_enter()
        acc.account_button_click()
        acc.wait_for_profile_site()
        acc.history_button_click()
        assert acc.wait_for_history_list()

    @allure.title('Выход из аккаунта')
    def test_personal_account_quit_button_click_success(self, driver):
        acc = AccountPage(driver)
        acc.login_open()
        acc.login_enter()
        acc.account_button_click()
        acc.wait_for_profile_site()
        acc.click_quit_button()
        assert acc.get_login_page()
