import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import RegisterPageLocators, LoginPageLocators, MainPageLocators
from helpers import generate_user_data
from constants import BASE_URL

class TestRegistration:
    def test_successful_registration(self, driver):
        user_data = generate_user_data()
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(user_data["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        # Проверка, что после регистрации перешли на страницу входа
        assert WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT))

    def test_registration_with_invalid_password(self, driver):
        user_data = generate_user_data()
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegisterPageLocators.NAME_INPUT)).send_keys(user_data["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        # Проверка появления сообщения об ошибке
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)).is_displayed()