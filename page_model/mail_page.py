import logging
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.mail_page import MailPageLocators
from utils import random_string_generator
from .base_page import BasePage


class MailPage(BasePage):
    @property
    def new_mail_button(self):
        return self.get_element_or_screenshot(MailPageLocators.NEW_MAIL_BUTTON)

    @property
    def recipient_field(self):
        return self.get_element_or_screenshot(MailPageLocators.RECIPIENT_FIELD)

    @property
    def subject_field(self):
        return self.get_element_or_screenshot(MailPageLocators.SUBJECT_FIELD)

    @property
    def cc_link(self):
        return self.get_element_or_screenshot(MailPageLocators.CC_LINK)

    @property
    def cc_field(self):
        return self.get_element_or_screenshot(MailPageLocators.CC_FIELD)

    @property
    def bcc_link(self):
        return self.get_element_or_screenshot(MailPageLocators.BCC_LINK)

    @property
    def bcc_field(self):
        return self.get_element_or_screenshot(MailPageLocators.BCC_FIELD)

    @property
    def body_field(self):
        return self.get_element_or_screenshot(MailPageLocators.BODY_FIELD)

    @property
    def send_button(self):
        return self.get_element_or_screenshot(MailPageLocators.SEND_BUTTON)

    def sent_email(self, text):
        return self.get_element_or_screenshot((By.XPATH, "//*/span[contains(text(), '{}')]".format(text)))


    def received_email(self, text):
        return self.get_element_or_screenshot((By.XPATH, "//*/b[contains(text(), '{}')]".format(text)))

    def element(self, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '{}')]".format(text)))
            )
            return True
        except:
            file_path = os.path.join(os.getcwd(), "logs", "screenshots",
                                     "{}.png".format(random_string_generator(size=5)))
            self.driver.save_screenshot(file_path)
            logging.error(
                "Element can't be located. Check screenshot for details: {}".format(file_path))
            return False
