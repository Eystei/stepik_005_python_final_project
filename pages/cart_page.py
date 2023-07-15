import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    main_word_cart_page = "(//h1[@class='title'])[2]"
    input_receiver_name = "(//span[@class='frame-form-field']//input)[1]"
    input_phone = "(//div[@class='d_b o_h']//input)[1]"
    input_email = "(//span[@class='frame-form-field']//input)[2]"
    frame_select_region = "(//div[@class='lineForm']//div)[1]"
    select_region = "//span[@val='5']"
    input_delivery_address = "(//span[@class='frame-form-field']//input)[3]"
    frame_select_payment = "(//div[@class='cuselText'])[2]"
    select_payment = "//span[@val='1']"
    accept_terms = "//input[@type='checkbox']"

    # GETTERS
    def get_main_word_cart_page(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_word_cart_page)))

    def get_input_receiver_name(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.input_receiver_name)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.input_phone)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.input_email)))

    def get_frame_select_region(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.frame_select_region)))

    def get_select_region(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_region)))

    def get_input_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.input_delivery_address)))

    def get_frame_select_payment(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.frame_select_payment)))

    def get_select_payment(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.select_payment)))

    def get_accept_terms(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.accept_terms)))

    # ACTIONS
    def fill_receiver_name(self, receiver_name):
        self.get_input_receiver_name().clear()
        self.get_input_receiver_name().send_keys(receiver_name)
        print("Input Receiver Name")

    def fill_input_phone(self, phone):
        self.get_input_phone().send_keys(phone)
        print("Input Phone")

    def fill_email(self, email):
        self.get_input_email().clear()
        self.get_input_email().send_keys(email)
        print("Input Receiver Name")

    def click_frame_select_region(self):
        self.get_frame_select_region().click()
        print("Click Frame Select Region")

    def click_get_select_region(self):
        region = self.get_select_region()
        self.driver.execute_script("arguments[0].click();", region)

    def fill_delivery_address(self, address):
        self.get_input_delivery_address().send_keys(address)
        print("Input Delivery Address")

    def click_frame_select_payment(self):
        self.get_frame_select_payment().click()
        print("Click Frame Select Payment")

    def click_select_payment(self):
        self.get_select_payment().click()
        print("Click Select Payment")

    def click_accept_terms(self):
        self.get_accept_terms().click()
        print("Click Accept Terms")

    # METHODS
    def make_order(self):
        self.driver.refresh()
        self.get_current_url()
        self.assert_url("https://redstore.am/en/shop/cart")
        self.assert_word(self.get_main_word_cart_page(), "Make order")
        self.fill_receiver_name("Angela Yu")
        self.fill_input_phone("+123456")
        self.fill_email("liridif903@niback.com")
        self.click_frame_select_region()
        self.click_get_select_region()
        self.fill_delivery_address("str.Bandanna, 18/2")
        self.click_frame_select_payment()
        self.click_select_payment()
        self.click_accept_terms()
        print("Final Action on Cart Page. I dont know how to handle Captcha.")
        time.sleep(1)

