from PomAdmin.Locators.locators import locator

class Profile():

    def __init__(self, driver):
        self.driver = driver
        self.welcome_Profile_link_id = locator.welcome_Profile_link_id
        self.logoutProfile_xpath = locator.logoutProfile_xpath

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_Profile_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logoutProfile_xpath).click()