from PomAdmin.Locators.locators import locator
from urlmatch import urlmatch
# from selenium.webdriver.common.alert import Alert

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.eMailAddress_textbox_id = locator.eMailAddress_textbox_id
        self.password_textbox_id = locator.password_textbox_id
        self.login_button_xpath = locator.login_button_xpath
        self.login_InvalidEmailMessage_xpath = locator.login_InvalidEmailMessage_xpath

    def enter_username(self, username):
        # self.driver.find_element_by_id(self.eMailAddress_textbox_id).clear()
        self.driver.find_element_by_id(self.eMailAddress_textbox_id).send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self, driver):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        get_url = driver.current_url
        print(get_url)
        match_pattern = "https://dev-admin.sympliant.com/"
        if urlmatch(match_pattern, get_url):
            loginInvalidEmail_message = self.driver.find_element_by_xpath(self.login_InvalidEmailMessage_xpath).text
            assert loginInvalidEmail_message == "These credentials do not match our records."
            print(loginInvalidEmail_message)
        else:
            print("pass")

    def click_loginalert(self, driver):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
        get_url = driver.current_url
        match_pattern = "https://dev-admin.sympliant.com/"
        if urlmatch(match_pattern, get_url):
            assert get_url == match_pattern
        else:
            print("pass")

