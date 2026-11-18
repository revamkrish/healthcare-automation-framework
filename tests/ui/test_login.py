from pages.login_page import LoginPage
from pages.appointment_page import AppointmentPage
from config import BASE_URL
import pytest
from test_data.login_data import (
    VALID_LOGIN,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_BOTH
)

@pytest.mark.parametrize("login_data", [
    VALID_LOGIN,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_BOTH
])
def test_login(driver, login_data):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.click_make_appointment()
    login_page.enter_username(login_data["username"])
    login_page.enter_password(login_data["password"])
    login_page.click_login()

    if login_data["expected"] == "success":
        appointment_page = AppointmentPage(driver)
        assert appointment_page.get_header_text() == "Make Appointment"

    else:
        assert "Login failed" in login_page.get_error_message()