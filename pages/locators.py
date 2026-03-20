from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href,'/') and text()='Конструктор']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo']/a")
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__')]//span")

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class ForgotPasswordPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href,'/') and text()='Конструктор']")
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo']/a")