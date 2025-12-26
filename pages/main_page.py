import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Принять cookie")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Кликнуть по кнопке 'Заказать' в header")
    def click_header_order(self):
        self.click(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Кликнуть по кнопке 'Заказать' в footer")
    def click_footer_order(self):
        # Прокручиваем к элементу перед кликом (он внизу страницы)
        self.scroll_to_element(MainPageLocators.FOOTER_ORDER_BUTTON) #!
        self.click(MainPageLocators.FOOTER_ORDER_BUTTON)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Кликнуть по вопросу {index} в FAQ")
    def click_faq_question(self, index):
        # Прокручиваем к FAQ секции
        self.scroll_to_element(MainPageLocators.FAQ_QUESTION(index)) #!
        self.click(MainPageLocators.FAQ_QUESTION(index))

    @allure.step("Получить текст ответа #{index} в FAQ")
    def get_faq_answer(self, index):
        element = self.find_element(MainPageLocators.FAQ_ANSWER(index))
        return element.text.strip()

    @allure.step("Перейти к оформлению заказа (is_header={is_header})")
    def go_to_order(self, is_header=True):
        if is_header:
            self.click_header_order()
        else:
            self.click_footer_order()
