from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).clear()
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self):
        return self.driver.title

    def is_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))