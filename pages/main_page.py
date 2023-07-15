import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    drop_menu_categories = "(//span[@class='text-el glav'])[2]"
    categories_notebooks = "[alt='Notebooks']"

    # GETTERS
    def get_drop_menu_categories(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.XPATH, self.drop_menu_categories)))

    def get_categories_notebooks(self):
        return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((By.CSS_SELECTOR, self.categories_notebooks)))

    # ACTIONS

    def click_drop_menu_categories(self):
        self.get_drop_menu_categories().click()
        print("Click Drop Menu Categories")

    def click_categories_notebooks(self):
        self.get_categories_notebooks().click()
        print("Click Category Notebooks")

    # METHODS

    def enter_to_notebook_category(self):
        time.sleep(3)
        self.click_drop_menu_categories()
        self.get_current_url()
        self.click_categories_notebooks()


