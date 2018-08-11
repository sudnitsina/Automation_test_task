from locators.login_page import LoginPageLocators

from .base_page import BasePage


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


