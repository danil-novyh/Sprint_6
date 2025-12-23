import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData

class TestOrderFlow:
    @allure.title("Позитивный сценарий оформления заказа")
    @pytest.mark.parametrize(
        "is_header, name, last_name, address, metro, phone, date, period, color, comment",
        OrderData.POSITIVE_CASES
    )
    def test_successful_order(
        self, driver, is_header, name, last_name, address, metro, phone, date, period, color, comment
    ):
        main = MainPage(driver)
        main.accept_cookies()
        if is_header:
            main.go_to_order_from_header()
        else:
            main.go_to_order_from_footer()

        order = OrderPage(driver)
        order.fill_first_form(name, last_name, address, metro, phone)
        order.fill_second_form(date, period, color, comment)
        assert order.is_order_success()
