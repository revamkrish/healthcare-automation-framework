from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AppointmentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.appointment_header = (By.TAG_NAME, "h2")

    def get_header_text(self):
        return self.get_text(self.appointment_header)