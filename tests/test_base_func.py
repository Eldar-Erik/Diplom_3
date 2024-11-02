import allure
from pages.home_page import HomePage


class TestBaseFunc:

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor_button_success(self, driver):
        base = HomePage(driver)
        base.login_open()
        base.click_constructor_button()
        base.wait_constructor_site()
        assert base.vis_constructor_site()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_orders_button_success(self, driver):
        base = HomePage(driver)
        base.home_open()
        base.click_order_list_button()
        assert base.get_order_list_toc()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_card_success(self, driver):
        base = HomePage(driver)
        base.home_open()
        base.click_on_ingredient()
        base.wait_for_ingredient_window()
        assert base.vis_toc()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_ingredient_card_close_success(self, driver):
        base = HomePage(driver)
        base.home_open()
        base.click_on_ingredient()
        base.wait_for_ingredient_window()
        base.vis_toc()
        base.close_ingredient_window()
        assert base.wait_constructor_site()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_counter_success(self, driver):
        base = HomePage(driver)
        base.home_open()
        base.wait_constructor_site()
        base.action_ingridient()
        assert base.get_ingredient_counter() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_user_order_success(self, driver):
        base = HomePage(driver)
        base.login_open()
        base.login_enter()
        base.action_ingridient()
        base.click_order_button()
        assert base.get_order_success()
