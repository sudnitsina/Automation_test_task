from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import get_screenshot


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return "https://mail.google.com"

    def get_element_or_screenshot(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except:
            get_screenshot(self.driver)