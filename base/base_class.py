import time


# python -m pytest -s -v

class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """Method Assert Words"""

    def assert_word(self, element, exp_result):
        value_word = element.text
        assert value_word == exp_result
        print("PASS     ELEMENT VALUE WORD ON CURRENT PAGE - CORRECT")

    """Method Screenshot"""

    def get_screenshot(self):
        self.driver.save_screenshot(f"./screenshots/screen {time.strftime('%Y_%m_%d %Hh%Mm%Ss')}.png")

    """Method Assert URL"""

    def assert_url(self, exp_result):
        current_url = self.driver.current_url
        assert current_url == exp_result
        print("PASS     CURRENT URL IS CORRECT")
