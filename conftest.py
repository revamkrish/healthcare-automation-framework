
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.api_client import APIClient
from config import API_BASE_URL


@pytest.fixture
def driver():

    options = Options()

    # Headless mode for CI/CD
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def api_client():
    return APIClient(API_BASE_URL)
