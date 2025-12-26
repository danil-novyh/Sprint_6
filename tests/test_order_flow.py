import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData

class TestOrderFlow:
    @allure.epic("Оформление заказа")
    @allure.feature("Полный флоу заказа")
    @allure.story("Позитивный сценарий")
    @allure.title("Заказ самоката: {entry_point_name}")
    @allure.description(
        "Проверка полного флоу оформления заказа с двумя наборами данных "
        "и двумя точками входа (верхняя и нижняя кнопки 'Заказать')"
    )
    @pytest.mark.parametrize(
        "is_header, name, last_name, address, metro, phone, date, period, color, comment",
        OrderData.POSITIVE_CASES, 
        ids=["Верхняя_кнопка", "Нижняя_кнопка"]
        )
    def test_successful_order(
        self, driver, is_header, name, last_name, address, metro, phone, date, period, color, comment
    ):
        # Определяем название точки входа для Allure отчёта
        entry_point_name = "Верхняя кнопка" if is_header else "Нижняя кнопка"
        allure.dynamic.parameter("entry_point_name", entry_point_name)
        # Создаем объекты страниц
        main = MainPage(driver)
        order = OrderPage(driver)
        # Принимаем cookie
        main.accept_cookies()
        # ИСПРАВЛЕНО, убраны условия
        main.go_to_order(is_header=is_header)
        # Заполнение форм
        order.fill_first_form(name, last_name, address, metro, phone)
        order.fill_second_form(date, period, color, comment)
        # Проверка успешного оформления
        assert order.is_order_success(), "Заказ был успешно оформлен"
