import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import random
import string
import requests

BASE_URL = "https://stellarburgers.education-services.ru"

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
def generate_user():
    first_name = "Anton"
    last_name = "Zakupnev"
    cohort = "42"
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    name = "Test User"
    return {"email": email, "password": password, "name": name}

@pytest.fixture
def create_user_via_api(generate_user):
    payload = {
        "email": generate_user["email"],
        "password": generate_user["password"],
        "name": generate_user["name"]
    }
    response = requests.post(f"{BASE_URL}/api/auth/register", json=payload)
    if response.status_code == 200:
        data = response.json()
        return {
            "email": generate_user["email"],
            "password": generate_user["password"],
            "name": generate_user["name"],
            "accessToken": data.get("accessToken"),
            "refreshToken": data.get("refreshToken")
        }
    else:
        raise Exception(f"Failed to create user via API: {response.text}")