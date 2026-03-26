import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from constants import BASE_URL

class TestLogin:
    def test_login_via_main_page_button(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        # Проверка, что после входа отображается кнопка "Оформить заказ"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()
        assert driver.current_url == f"{BASE_URL}/"

    def test_login_via_personal_account_button(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()
        assert driver.current_url == f"{BASE_URL}/"

    def test_login_via_register_page_button(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()
        assert driver.current_url == f"{BASE_URL}/"

    def test_login_via_forgot_password_page_button(self, driver, create_user_via_api_fixture):
        user = create_user_via_api_fixture
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)).is_displayed()
        assert driver.current_url == f"{BASE_URL}/"