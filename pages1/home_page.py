from selenium.webdriver.common.by import By
from pages1.base_page import BasePage

class HomePage(BasePage):
    SIGNUP_BUTTON = (By.LINK_TEXT, "Sign up")
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        super().__init__(driver)

    def click_signup(self):
        self.click(self.SIGNUP_BUTTON)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_homepage_title(self):
        return self.get_title()

