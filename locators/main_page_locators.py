from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    HEADER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    FOOTER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    LOGO_SCOOTER = (By.XPATH, "//a[@href='/']")
    LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru']")

    @staticmethod
    def FAQ_QUESTION(index):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def FAQ_ANSWER(index):
        return (By.ID, f"accordion__panel-{index}")
