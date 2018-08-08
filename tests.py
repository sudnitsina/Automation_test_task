import logging
# import time
from datetime import datetime

import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver

from page_model.login_page import LoginPage, MailPage
from utils import get_test_data

logging.basicConfig(filename="logs/pytest.log", level=logging.INFO)


class TestGmail:
    """
    Check that email can be sent and received using gmail service

    """
    @pytest.mark.parametrize("from_username, from_password, to_username, to_password", get_test_data())
    def test_mail(self, from_username, from_password, to_username, to_password):
        gmail_url = "https://mail.google.com/"
        logging.getLogger(__name__)
        logging.info(
            "TestGmail started for the dataset: {}".format((from_username, from_password, to_username, to_password)))

        today = datetime.today()
        from_email = "{}@gmail.com".format(from_username)
        to_email = "{}@gmail.com".format(to_username)
    
        self.driver = WebDriver()
        browser = self.driver.desired_capabilities["browserName"]
        mail_text = "{}-{}".format(browser, today)
        logging.info("Opening {}".format(gmail_url))
        self.driver.get(gmail_url)
        page = LoginPage(self.driver)
        logging.info("Inserting username")
        page.username.send_keys(from_username, Keys.RETURN)
        # time.sleep(1)  # sleep to avoid 405 response
        logging.info("Inserting password")
        page.password.send_keys(from_password, Keys.RETURN)

        # send mail
        page = MailPage(self.driver)
        page.new_mail_button.click()

        logging.info("Filling mail form")
        page.recipient_field.click()
        page.recipient_field.send_keys(to_email)
        page.cc_link.click()
        page.cc_field.send_keys(to_email)
        page.bcc_link.click()
        page.bcc_field.send_keys(to_email)
        page.subject_field.send_keys(mail_text)
        page.body_field.click()
        page.body_field.send_keys(mail_text)

        logging.info("Sending mail with text '{}'".format(mail_text))
        page.send_button.click()
        assert page.element("Your message has been sent")
    
        # check mail in sent
        url = "https://mail.google.com/mail/#sent"
        self.driver.get(url)
        page = MailPage(self.driver)
        logging.info("Checking mail in sent")
        assert page.element(mail_text)
        self.driver.quit()

        # login to second account
        self.driver = WebDriver()
        logging.info("Opening {}".format(gmail_url))
        self.driver.get(gmail_url)
        page = LoginPage(self.driver)
        logging.info("Inserting username")
        page.username.send_keys(to_username, Keys.RETURN)
        # time.sleep(1)   # sleep to avoid 405 response
        logging.info("Inserting password")
        page.password.send_keys(to_password, Keys.RETURN)
        page = MailPage(self.driver)

        logging.info("Opening email")
        page.received_email(mail_text).click()

        logging.info("Checking text")
        assert page.element(mail_text)
        logging.info("Checking sender")
        assert page.element(from_email)

        logging.info("test passed")

    def teardown(self):
        self.driver.quit()
