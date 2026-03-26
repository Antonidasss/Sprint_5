import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from constants import BASE_URL

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Проверка наличия кнопки "Выход"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)).is_displayed()
        assert "account" in driver.current_url

    def test_exit_from_account(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Клик по кнопке "Выход"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()
        # Проверка перехода на страницу логина
        assert WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "login" in driver.current_url

    def test_go_to_constructor_from_account(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Клик по "Конструктор"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ProfilePageLocators.CONSTRUCTOR_LINK_GENERIC)).click()
        # Проверка URL
        assert WebDriverWait(driver, 5).until(EC.url_to_be(f"{BASE_URL}/"))
        assert driver.current_url == f"{BASE_URL}/"

    def test_go_to_constructor_via_logo(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Клик по логотипу
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ProfilePageLocators.LOGO_LINK)).click()
        # Проверка URL
        assert WebDriverWait(driver, 5).until(EC.url_to_be(f"{BASE_URL}/"))
        assert driver.current_url == f"{BASE_URL}/"