from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    url = "https://redstore.am/en/"

    # CREDENTIALS
    cred_email = "liridif903@niback.com"
    cred_pass = "liridif903"

    # LOCATORS
    button_login = "#loginButton"
    input_email = "input[name='email']"
    input_password = "input[type='password']"
    button_submit_login = "(//span[text()='Login'])[2]"
    main_word = "[class='success success'] .text-el"

    # GETTERS
    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.button_login)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.input_email)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.input_password)))

    def get_button_submit_login(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.button_submit_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.main_word)))

    # ACTIONS

    def click_button_login(self):
        self.get_button_login().click()
        print("Click Button Login")

    def fill_email(self, email):
        self.get_input_email().clear()
        self.get_input_email().send_keys(email)
        print("Input Email")

    def fill_password(self, password):
        self.get_input_password().clear()
        self.get_input_password().send_keys(password)
        print("Input Password")

    def click_button_submit_login(self):
        self.get_button_submit_login().click()
        print("Click Button Submit Login")

    # METHODS
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.assert_url("https://redstore.am/en")
        self.click_button_login()
        self.fill_email("liridif903@niback.com")
        self.fill_password("liridif903")
        self.click_button_submit_login()
        self.assert_word(self.get_main_word(), "User successfully logged in")
