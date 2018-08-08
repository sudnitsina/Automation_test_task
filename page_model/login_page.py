import logging
import os
import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.login_page import LoginPageLocators, MailPageLocators


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


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
            file_name = "logs/screenshots/{}.png".format(random_string_generator(size=5))
            self.driver.save_screenshot(file_name)
            logging.error(
                "Element can't be located. Check screenshot for details: file://{0}/{1}".format(os.getcwd(), file_name))


class LoginPage(BasePage):
    @property
    def url(self):
        return "https://accounts.google.com/"

    @property
    def username(self):
        return self.get_element_or_screenshot(LoginPageLocators.USERNAME_FIELD)

    @property
    def password(self):
        return self.get_element_or_screenshot(LoginPageLocators.PASSWORD_FIELD)


class MailPage(BasePage):
    @property
    def url(self):
        return "https://mail.google.com"

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
            file_name = "logs/screenshots/{}.png".format(random_string_generator(size=5))
            self.driver.save_screenshot(file_name)
            logging.error(
                "Element can't be located. Check screenshot for details: file://{0}/{1}".format(os.getcwd(), file_name))
            return False
