import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from constants import BASE_URL

class TestConstructorSections:
    def test_switch_to_buns(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)).click()
        active = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Булки" in active.text

    def test_switch_to_sauces(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)).click()
        active = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Соусы" in active.text

    def test_switch_to_fillings(self, driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)).click()
        active = WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.ACTIVE_SECTION))
        assert "Начинки" in active.text