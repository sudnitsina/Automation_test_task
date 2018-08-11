from utils import random_string_generator
from selenium.webdriver.support.ui import WebDriverWait
import os
import logging
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element_or_screenshot(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except:
            file_path = os.path.join(os.getcwd(), "logs", "screenshots",
                                     "{}.png".format(random_string_generator(size=5)))
            self.driver.save_screenshot(file_path)
            logging.error(
                "Element can't be located. Check screenshot for details: {}".format(file_path))