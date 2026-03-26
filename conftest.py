import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from helpers import generate_user_data, create_user_via_api
from constants import BASE_URL

@pytest.fixture(params=["chrome"], scope="function")
def driver(request):
    browser = request.param
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def create_user_via_api_fixture():
    """Фикстура для создания пользователя через API (предусловие)"""
    user_data = generate_user_data()
    user = create_user_via_api(user_data)
    return user