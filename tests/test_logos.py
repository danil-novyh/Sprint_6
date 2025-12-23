import allure
from pages.main_page import MainPage

from urls import Urls

class TestLogos:
    @allure.title("Клик по логотипу «Самокат» ведёт на главную")
    def test_scooter_logo_redirects_to_main(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.go_to_order_from_header()
        main.click_scooter_logo()
        assert main.current_url() == Urls.MAIN

    @allure.title("Клик по логотипу «Яндекс» открывает Дзен")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main = MainPage(driver)
        main.accept_cookies()
        main.click_yandex_logo()
        main.switch_to_new_tab()

        main.wait_for_url_contains("dzen")
