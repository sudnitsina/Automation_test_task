from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = By.XPATH, '//*[@id="identifierId"]'
    PASSWORD_FIELD = By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'
