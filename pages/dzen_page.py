from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators

class DzenPage(BasePage):
    def is_dzen_loaded(self):
        return self.find_element(DzenPageLocators.DZEN_LOGO).is_displayed()