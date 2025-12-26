import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнить первую форму (Для кого самокат)")
    def fill_first_form(self, name, last_name, address, metro, phone):
        self.set_text(OrderPageLocators.NAME, name)
        self.set_text(OrderPageLocators.LAST_NAME, last_name)
        self.set_text(OrderPageLocators.ADDRESS, address)
        self.click(OrderPageLocators.METRO_INPUT)
        # ИСПРАВЛЕНО
        metro_locator = OrderPageLocators.get_metro_station_locator(metro)
        self.click(metro_locator)
        self.set_text(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму (Про аренду)")
    def fill_second_form(self, date, period, color, comment):
        date_field = self.find_element(OrderPageLocators.DATE)
        date_field.clear()
        date_field.send_keys(date)
        # ИСПРАВЛЕНО
        # Клик вне поля для закрытия календаря
        self.click(OrderPageLocators.PRO_ARENDU_HEADER)
        self.click(OrderPageLocators.RENTAL_PERIOD)
        # ИСПРАВЛЕНО
        period_locator = OrderPageLocators.get_rental_period_locator(period)
        self.click(period_locator)
        if color == "black":
            self.click(OrderPageLocators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click(OrderPageLocators.GREY_CHECKBOX)
        if comment:
            self.set_text(OrderPageLocators.COMMENT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        # Ждем появления окна
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.CONFIRM_MODAL_TEXT))
        # ИСПРАВЛЕНО: Используем self.js_click
        self.js_click(OrderPageLocators.CONFIRM_BUTTON)
        # ИСПРАВЛЕНО. Ждём успех
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL))

    @allure.step("Проверить успешное оформление заказа")
    def is_order_success(self):
        return "Заказ оформлен" in self.get_text(OrderPageLocators.SUCCESS_MODAL)
