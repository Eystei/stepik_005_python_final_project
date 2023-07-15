from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.notebook_page import NotebookPage
from pages.cart_page import CartPage
from selenium.webdriver.chrome.options import Options

import time

driver = webdriver.Chrome()
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")


def test_buy_product():
    login = LoginPage(driver=driver)
    login.authorization()

    main_page = MainPage(driver)
    main_page.enter_to_notebook_category()

    notebook_page = NotebookPage(driver)
    notebook_page.enter_to_notebook_category()

    cart_page = CartPage(driver)
    cart_page.make_order()

    time.sleep(5)

    print("FINISH")
