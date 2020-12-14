from PomAdmin.Locators.locators import locator
from selenium.webdriver.common.action_chains import ActionChains
from urlmatch import urlmatch

class IDN():
    def __init__(self, driver):
        self.driver = driver
        self.IDN_Button_xpath = locator.IDN_Button_xpath
        self.IDN_Create_Button_xpath = locator.IDN_Create_Button_xpath
        self.IDN_Create_Textbox_xpath = locator.IDN_Create_Textbox_xpath
        self.IDN_Create_description_Textbox_id = locator.IDN_Create_description_Textbox_id
        self.IDN_Submit_Button_xpath = locator.IDN_Submit_Button_xpath
        # it will run. If the message come IDNName "The name has already been taken.".
        self.IDN_Already_textmessage_xpath = locator.IDN_Already_textmessage_xpath

    def idn_selection(self):
        self.driver.find_element_by_xpath(self.IDN_Button_xpath).click()

    def idn_selection_create(self, driver):
        idnelement = self.driver.find_element_by_xpath(self.IDN_Create_Button_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(idnelement).click()
        actions.perform()

    def idn_create_text(self, Idn_text):
        self.driver.find_element_by_xpath(self.IDN_Create_Textbox_xpath).send_keys(Idn_text)

    def idn_description_text(self, Desc_text):
        self.driver.find_element_by_id(self.IDN_Create_description_Textbox_id).send_keys(Desc_text)

    def idn_submit(self, driver):
        self.driver.find_element_by_xpath(self.IDN_Submit_Button_xpath).click()
        get_url = driver.current_url
        print(get_url)
        match_pattern = "https://dev-admin.sympliant.com/idns/create"
        if urlmatch(match_pattern, get_url):
            idn_message = self.driver.find_element_by_xpath(self.IDN_Already_textmessage_xpath).text
            assert idn_message == "The name has already been taken."
            print(idn_message)
        else:
            print("pass")
