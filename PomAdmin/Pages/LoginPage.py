from PomAdmin.Locators.locators import locator
class LoginPaget():

    def __init__(self, driver):
        self.driver = driver
        self.eMailAddress_textbox_id = locator.eMailAddress_textbox_id
        self.password_textbox_id = locator.password_textbox_id
        self.login_button_xpath = locator.login_button_xpath

    def enter_username(self, username):
        # self.driver.find_element_by_id(self.eMailAddress_textbox_id).clear()
        self.driver.find_element_by_id(self.eMailAddress_textbox_id).send_keys(username)

    def enter_password(self, password):
        # self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()