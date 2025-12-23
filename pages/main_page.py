from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    def click_header_order(self):
        self.click(MainPageLocators.HEADER_ORDER_BUTTON)

    def click_footer_order(self):
        self.click(MainPageLocators.FOOTER_ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    def click_faq_question(self, index):
        self.click(MainPageLocators.FAQ_QUESTION(index))

    def get_faq_answer(self, index):
        element = self.find_element(MainPageLocators.FAQ_ANSWER(index))
        return element.text.strip()

    def go_to_order_from_header(self):
        self.click_header_order()

    def go_to_order_from_footer(self):
        self.click_footer_order()
