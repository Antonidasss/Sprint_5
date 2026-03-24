import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators, LoginPageLocators
from constants import BASE_URL

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, create_user_via_api):
        user = create_user_via_api
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Проверка наличия кнопки "Выход"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']"))).is_displayed()
        assert "account" in driver.current_url

    def test_exit_from_account(self, driver, create_user_via_api):
        user = create_user_via_api
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Клик по кнопке "Выход"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))).click()
        # Проверка перехода на страницу логина
        assert WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "login" in driver.current_url

    def test_go_to_constructor_from_account(self, driver, create_user_via_api):
        user = create_user_via_api
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Клик по "Конструктор"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Конструктор')]"))).click()
        # Проверка URL
        assert WebDriverWait(driver, 5).until(EC.url_to_be(f"{BASE_URL}/"))
        assert driver.current_url == f"{BASE_URL}/"

    def test_go_to_constructor_via_logo(self, driver, create_user_via_api):
        user = create_user_via_api
        driver.get(BASE_URL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN)).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        # Клик по логотипу
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/']"))).click()
        # Проверка URL
        assert WebDriverWait(driver, 5).until(EC.url_to_be(f"{BASE_URL}/"))
        assert driver.current_url == f"{BASE_URL}/"