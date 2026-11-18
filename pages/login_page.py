from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # Locators
    USERNAME = (By.ID, "txt-username")
    PASSWORD = (By.ID, "txt-password")
    LOGIN_BUTTON = (By.ID, "btn-login")
    MAKE_APPOINTMENT = (By.ID, "btn-make-appointment")

    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-danger")

    def __init__(self, driver):
        super().__init__(driver)

    def click_make_appointment(self):
        self.click(self.MAKE_APPOINTMENT)

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)