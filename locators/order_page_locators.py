from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    @staticmethod
    def get_metro_station_locator(station_name: str):
        return (By.XPATH, f"//div[text()='{station_name}']")
    
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_OPTION = lambda text: (By.XPATH, f"//div[text()='{text}']")
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//*[text()='Заказ оформлен']")
    
    @staticmethod
    def get_rental_period_locator(period: str):
        return (By.XPATH, f"//div[text()='{period}']")
    
    CONFIRM_MODAL_TEXT = (By.XPATH, "//*[text()='Хотите оформить заказ?']")
    PRO_ARENDU_HEADER = (By.XPATH, "//div[text()='Про аренду']")