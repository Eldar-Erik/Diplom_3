'''Проверь:
-ввод почты и клик по кнопке «Восстановить»,
-клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.'''
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
