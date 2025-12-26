from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def set_text(self, locator, text):
        el = self.find_element(locator)
        el.clear()
        el.send_keys(text)
        return el  # ДОБАВЛЕНО

    def get_text(self, locator):
        return self.find_element(locator).text

    def current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url_contains(self, part):
        self.wait.until(EC.url_contains(part))
    
    def js_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        