from selenium.webdriver.common.by import By


class MailPageLocators:
    NEW_MAIL_BUTTON = By.XPATH, "//*[contains(text(), 'COMPOSE')]"
    RECIPIENT_FIELD = By.CSS_SELECTOR, 'textarea[aria-label=To]'
    SUBJECT_FIELD = By.CSS_SELECTOR, 'input[name=subjectbox]'
    CC_LINK = By.CSS_SELECTOR, 'span[aria-label="Add Cc Recipients ‪(Ctrl-Shift-C)‬"]'
    CC_FIELD = By.CSS_SELECTOR, 'textarea[aria-label=Cc]'
    BCC_LINK = By.XPATH, "//*[contains(text(), 'Bcc')]"
    BCC_FIELD = By.CSS_SELECTOR, 'textarea[aria-label=Bcc]'
    BODY_FIELD = By.CSS_SELECTOR, 'div[aria-label="Message Body"]'
    SEND_BUTTON = By.XPATH, "//*[contains(text(), 'Send')]"
    SENT_MAIL_LINK = By.CSS_SELECTOR, 'a[title="Sent Mail"]'
