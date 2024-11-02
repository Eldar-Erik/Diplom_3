import allure
from pages.orders_page import OrderPage


class TestOrderPage:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_tag_window_true(self, driver):
        order = OrderPage(driver)
        order.login_open()
        order.login_enter()
        order.click_order_list_button()
        order.clico_order_cont()
        assert order.vis_tag_window()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_num_history_eq_order_num_list_success(self, driver):
        order = OrderPage(driver)
        order.login_open()
        order.login_enter()
        order.action_ingridient()
        order.click_order_button()
        order.wait_order_prepare()
        order.close_order_prepare_window()
        order.account_button_click()
        order.history_button_click()
        order.wait_for_history_list()
        order.scroll_down_order_list()
        history_order = order.get_order_from_history()
        order.click_order_list_button()
        list_order = order.get_order_from_list()
        assert history_order == list_order

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_orders_counter_success(self, driver):
        order = OrderPage(driver)
        order.login_open()
        order.login_enter()
        order.click_order_list_button()
        orders_before = order.get_orders_from_list()
        order.click_constructor_button()
        order.wait_constructor_site()
        order.action_ingridient()
        order.click_order_button()
        order.wait_order_prepare()
        order.close_order_prepare_window()
        order.click_order_list_button()
        orders_after = order.get_orders_from_list()
        assert orders_before < orders_after

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_orders_counter_success(self, driver):
        order = OrderPage(driver)
        order.login_open()
        order.login_enter()
        order.click_order_list_button()
        orders_before = order.get_today_orders_from_list()
        order.click_constructor_button()
        order.wait_constructor_site()
        order.action_ingridient()
        order.click_order_button()
        order.wait_order_prepare()
        order.close_order_prepare_window()
        order.click_order_list_button()
        orders_after = order.get_today_orders_from_list()
        assert orders_before < orders_after

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_numer_in_work_true(self, driver):
        order = OrderPage(driver)
        order.login_open()
        order.login_enter()
        order.action_ingridient()
        order.click_order_button()
        order.wait_order_prepare()
        order_by_order = order.get_order_numer_by_order()
        order.close_order_prepare_window()
        order.click_order_list_button()
        order.wait_for_numer_in_work()
        order_in_work = order.get_order_numer_in_work()
        assert order_by_order in order_in_work
