from PomAdmin.Locators.locators import locator
from selenium.webdriver.common.action_chains import ActionChains
from urlmatch import urlmatch

class hRegions():
    def __init__(self, driver):
        self.driver = driver
        self.hRegions_xpath = locator.hRegions_xpath
        self.hRegions_Create_xpath = locator.hRegions_Create_xpath
        self.hRegions_name_id = locator.hRegions_name_id
        self.hRegions_description_id = locator.hRegions_description_id
        self.hRegions_Submit_Button_xpath = locator.hRegions_Submit_Button_xpath
        # it will run. If the message come hRegionsName "The name has already been taken.".
        self.hRegions_Already_textmessage_xpath = locator.hRegions_Already_textmessage_xpath


    def hRegions_selection(self):
        self.driver.find_element_by_xpath(self.hRegions_xpath).click()

    def hRegions_create(self, driver):
        hRegionselement = self.driver.find_element_by_xpath(self.hRegions_Create_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(hRegionselement).click()
        actions.perform()

    def hRegions_name(self, regionsName):
        self.driver.find_element_by_id(self.hRegions_name_id).send_keys(regionsName)

    def hRegions_description(self, regionsDescription):
        self.driver.find_element_by_id(self.hRegions_description_id).send_keys(regionsDescription)

    def hRegions_Submit(self, driver):
        self.driver.find_element_by_xpath(self.hRegions_Submit_Button_xpath).click()
        get_url = driver.current_url
        print(get_url)
        match_pattern = "https://dev-admin.sympliant.com/idns/create"
        if urlmatch(match_pattern, get_url):
            hRegionsname_message = self.driver.find_element_by_xpath(self.hRegions_Already_textmessage_xpath).text
            assert hRegionsname_message == "The name has already been taken."
            print(hRegionsname_message)
        else:
            print("pass")