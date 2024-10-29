import allure
from pages.recovery_page import RecoveryPass
from src.data import URL_PASS_REC


class TestPassRecovery:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_pass_recovery_button_success(self, driver):
        rec = RecoveryPass(driver)
        rec.login_open()
        rec.click_rec_link()
        rec.visibility_pass_rec()
        assert rec.get_current_url() == URL_PASS_REC

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_data_recovery_button_success(self, driver):
        rec = RecoveryPass(driver)
        rec.rec_open()
        rec.send_email()
        rec.press_rec_button()
        assert rec.get_save_button()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_hide_pass_button_active_success(self, driver):
        rec = RecoveryPass(driver)
        rec.rec_open()
        rec.send_email()
        rec.press_rec_button()
        rec.press_vis_button()
        assert rec.get_active_cont()