import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def fill_first_form(self, name, last_name, address, metro, phone):
        self.set_text(OrderPageLocators.NAME, name)
        self.set_text(OrderPageLocators.LAST_NAME, last_name)
        self.set_text(OrderPageLocators.ADDRESS, address)
        self.click(OrderPageLocators.METRO_INPUT)
        self.click((By.XPATH, f"//div[text()='{metro}']"))
        self.set_text(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, period, color, comment):
        date_field = self.find_element(OrderPageLocators.DATE)
        date_field.clear()
        date_field.send_keys(date)
        self.click((By.XPATH, "//div[text()='Про аренду']"))
        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.click(OrderPageLocators.RENTAL_OPTION(period))
        if color == "black":
            self.click(OrderPageLocators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click(OrderPageLocators.GREY_CHECKBOX)
        if comment:
            self.set_text(OrderPageLocators.COMMENT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        # Ждем появления окна
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Хотите оформить заказ?']")))
        #
        # НАЖИМАЕМ "Да" ТОЛЬКО В ЭТОМ ОКНЕ
        confirm_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'Order_Buttons__')]//button)[last()]"))
        )
        self.driver.execute_script("arguments[0].click();", confirm_button)
        # Ждём успех
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Заказ оформлен']")))

    def is_order_success(self):
        return "Заказ оформлен" in self.get_text(OrderPageLocators.SUCCESS_MODAL)

