from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class NotebookPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    main_word_notebooks_page = "//h1[@class='title']"
    filter_notebook_acer = ".brand301"
    filter_notebook_hp = ".brand298"
    filter_notebook_apple = ".brand294"
    filter_price_min = ".minCost"
    filter_price_max = ".maxCost"
    filter_cpu_m1 = "(//span[text()='M1'])[1]"
    filter_ram_8gb = "//span[text()='8GB LPDDR4']"
    filter_touch_screen_no = "//span[text()='No']"
    filter_os_macos_big_sur = "//span[text()='macOS Big Sur']"
    button_buy_model_first = "(//button[@class='btnBuy infoBut'])[1]"
    button_buy_model_second = "(//button[@class='btnBuy infoBut'])[2]"
    button_back_to_shopping = "(//div[@class='btn-trans f_l']//span)[1]"
    button_make_order = "//div[@class='btn-buy f_r']//a[1]"

    # GETTERS

    def get_main_word_notebooks_page(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.main_word_notebooks_page)))

    def get_filter_notebook_acer(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filter_notebook_acer)))

    def get_filter_notebook_hp(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filter_notebook_hp)))

    def get_filter_notebook_apple(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filter_notebook_apple)))

    def get_filter_price_min(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filter_price_min)))

    def get_filter_price_max(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.filter_price_max)))

    def get_filter_cpu_m1(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_cpu_m1)))

    def get_filter_ram_8gb(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_ram_8gb)))

    def get_filter_touch_screen_no(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_touch_screen_no)))

    def get_filter_os_macos_big_sur(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.filter_os_macos_big_sur)))

    def get_button_buy_model_first(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.button_buy_model_first)))

    def get_button_buy_model_second(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.button_buy_model_second)))

    def get_button_back_to_shopping(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.button_back_to_shopping)))

    def get_button_make_order(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.button_make_order)))

    # ACTIONS

    def click_filter_notebook_acer(self):
        self.get_filter_notebook_acer().click()
        print("Click Filter Notebook Acer")

    def click_filter_notebook_hp(self):
        self.get_filter_notebook_hp().click()
        print("Click Filter Notebook HP")

    def click_filter_notebook_apple(self):
        self.get_filter_notebook_apple().click()
        print("Click Filter Notebook Apple")

    def input_filter_price_min(self, min_price):
        self.get_filter_price_min().clear()
        self.get_filter_price_min().send_keys(str(min_price))
        print("Input Filter Price Min")

    def input_filter_price_max(self, max_price):
        self.get_filter_price_max().clear()
        self.get_filter_price_max().send_keys(str(max_price))
        print("Input Filter Price Max")

    def click_filter_cpu_m1(self):
        self.get_filter_cpu_m1().click()
        print("Click Filter CPU M1")

    def click_filter_ram_8gb(self):
        self.get_filter_ram_8gb().click()
        print("Click Filter RAM 8GB DDR4")

    def click_filter_touch_screen_no(self):
        self.get_filter_touch_screen_no().click()
        print("Click Filter Touch Screen - No")

    def click_filter_os_macos_big_sur(self):
        self.get_filter_os_macos_big_sur().click()
        print("Click Filter OS MacOS Big Sur")

    def click_button_buy_model_first(self):
        self.get_button_buy_model_first().click()
        print("Click Button Model First")

    def click_button_buy_model_second(self):
        self.get_button_buy_model_second().click()
        print("Click Button Model Second")

    def click_button_back_to_shopping(self):
        self.get_button_back_to_shopping().click()
        print("Click Button Back to Shopping")

    def click_button_make_order(self):
        self.get_button_make_order().click()
        print("Click Button Make Order")

    # METHODS

    def enter_to_notebook_category(self):
        self.get_current_url()
        self.assert_url("https://redstore.am/en/shop/category/categories/notebooks")
        self.assert_word(self.get_main_word_notebooks_page(), "Notebooks")
        self.click_filter_notebook_acer()
        self.click_filter_notebook_hp()
        self.click_filter_notebook_apple()
        self.input_filter_price_min(100)
        self.input_filter_price_max(2_500_000)
        self.click_filter_cpu_m1()
        self.click_filter_ram_8gb()
        self.click_filter_touch_screen_no()
        self.click_filter_os_macos_big_sur()
        self.click_button_buy_model_first()
        self.click_button_back_to_shopping()
        self.click_button_buy_model_second()
        self.click_button_make_order()
