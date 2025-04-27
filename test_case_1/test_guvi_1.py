from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages1.home_page import HomePage
from pages1.login_page import LoginPage

class TestGuvi:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.guvi.in/")
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        print("\nClosing browser...")
        self.driver.quit()

    def test_case_1_load_home_page(self):
        assert "GUVI" in self.driver.title
        print("Test Case 1 Passed: Home page loaded.")

    def test_case_2_page_title(self):
        expected_title = "GUVI | Learn to code in your native language"
        actual_title = self.driver.title
        print(f"Test Case 2: Page Title = {actual_title}")

        assert actual_title == expected_title, f"Test Case 2 Failed: Expected '{expected_title}' but got '{actual_title}'."
        print("Test Case 2 Passed: Correct title shown.")

    def test_case_3_login_button_visibility(self):
        try:
            login_button = self.driver.find_element(By.LINK_TEXT, "Login")
            assert login_button.is_displayed() and login_button.is_enabled(), "Login button is either not visible or not clickable."
            print("Test Case 3 Passed: Login button is visible and clickable.")
        except NoSuchElementException:
            print("Test Case 3 Failed: Login button not found.")
            assert False, "Login button not found on the page."

    def test_case_4_click_signup_button(self):
        self.home_page.click_signup()
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        print("Test Case 2 Passed: Sign Up page opened.")

    def test_case_5_open_signup_modal(self):
        try:
            sign_up_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign up')]")) )
            sign_up_button.click()
            self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
            print("Test Case 5 Passed: Sign-Up modal opened successfully.")
        except TimeoutException:
            print("Test Case 5 Failed: Sign-Up modal did not open.")
            assert False, "Sign-Up modal did not open within expected time."
        except Exception as e:
            print(f"Test Case 5 Error: Unexpected error occurred - {e}")
            assert False, f"Unexpected Error: {e}"

    def test_case_6_valid_login(self):
        self.driver.get("https://www.guvi.in/sign-in/")
        self.login_page.login_valid_user("balajivenkat132002@gmail.com", "Balaji@13")
        self.wait.until(lambda driver: "dashboard" in driver.current_url or "Hi" in driver.page_source)
        print("Test Case 3 Passed: Valid login successful.")

    def test_case_7_invalid_login(self):
        self.driver.get("https://www.guvi.in/sign-in/")
        self.login_page.login_invalid_user("invalid_email@example.com", "wrongpassword")
        try:
            # Wait up to 30 seconds for any error text to appear in the page source
            WebDriverWait(self.driver, 30).until(
                lambda driver: "invalid" in driver.page_source.lower()
                               or "incorrect" in driver.page_source.lower()
                               or "wrong" in driver.page_source.lower()
            )
            print("Test Case 7 Passed: Error message detected after invalid login.")
        except TimeoutException:
            # Print page source for debugging
            print("\n========= PAGE SOURCE START =========\n")
            print(self.driver.page_source)
            print("\n========= PAGE SOURCE END =========\n")
            # Optionally take screenshot
            self.driver.save_screenshot('invalid_login_error.png')
            print("Screenshot saved: invalid_login_error.png")
            assert False, "No error message text found after invalid login."


if __name__ == "__main__":
    test = TestGuvi()
    test.setup_method()
    test.test_case_1_load_home_page()
    test.test_case_2_page_title()
    test.test_case_3_login_button_visibility()
    test.test_case_4_click_signup_button()
    test.test_case_5_open_signup_modal()
    test.test_case_6_valid_login()
    test.test_case_7_invalid_login()
    test.teardown_method()








