import allure
from pages.main_page import MainPage

from urls import Urls

class TestLogos:
    @allure.epic("Навигация")
    @allure.feature("Логотипы")
    @allure.story("Редирект на главную")
    @allure.title("Клик по логотипу «Самокат» ведёт на главную")
    def test_scooter_logo_redirects_to_main(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.go_to_order(is_header=True)
        main.click_scooter_logo()
        # Проверяем, что вернулись на главную
        current_url = main.current_url().rstrip('/')
        expected_url = Urls.MAIN.rstrip('/')
        
        assert current_url == expected_url, (
            f"После клика по логотипу 'Самокат' ожидался URL {expected_url}, "
            f"но получен {current_url}"
        )

    @allure.epic("Навигация")
    @allure.feature("Логотипы")
    @allure.story("Редирект на Дзен")
    @allure.title("Клик по логотипу «Яндекс» открывает Дзен")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_yandex_logo()
        main.switch_to_new_tab()

        main.wait_for_url_contains("dzen")
        # ИСПРАВЛЕНО. Добавлена явная проверка URL
        current_url = main.current_url()
        
        assert "dzen" in current_url, (
            f"После клика по логотипу 'Яндекс' ожидался URL с 'dzen', "
            f"но получен {current_url}"
        )
