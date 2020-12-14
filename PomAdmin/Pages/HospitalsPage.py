from PomAdmin.Locators.locators import locator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from urlmatch import urlmatch

class hospital():
    def __init__(self, driver):
        self.driver = driver
        self.Hospital_xpath = locator.Hospital_xpath
        self.Hospitals_Create_xpath = locator.Hospitals_Create_xpath
        self.Hospitals_Idn_Select_Id = locator.Hospitals_Idn_Select_Id
        self.Hospitals_Region_Select_id = locator.Hospitals_Region_Select_id
        self.Hospital_name_xpath = locator.Hospital_name_xpath
        self.Hospital_Description_xpath = locator.Hospital_Description_xpath
        self.Hospital_Phone_xpath = locator.Hospital_Phone_xpath
        self.Hospital_StreetAddress_xpath = locator.Hospital_StreetAddress_xpath
        self.Hospital1_StreetAddress_xpath = locator.Hospital1_StreetAddress_xpath
        self.Hospital_City_xpath = locator.Hospital_City_xpath
        self.Hospital_PostCode_xpath = locator.Hospital_PostCode_xpath
        self.Hospital_State_id = locator.Hospital_State_id
        self.Hospital_Country_id = locator.Hospital_Country_id
        self.Hospital_Submit_Button_xpath = locator.Hospital_Submit_Button_xpath
        # it will run. If the message come HospitalName "The name has already been taken.".
        self.Hospital_Already_textmessage_xpath = locator.Hospital_Already_textmessage_xpath

    def hospital_selection(self):
        print("hi")
        self.driver.find_element_by_xpath(self.Hospital_xpath).click()

    def hospital_create(self, driver):
        hospitalelement = self.driver.find_element_by_xpath(self.Hospitals_Create_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(hospitalelement).click()
        actions.perform()

    def hospital_select_Idn(self, index):
        Select_Idn = Select(self.driver.find_element_by_id(self.Hospitals_Idn_Select_Id))
        Select_Idn.select_by_index(index)

    def hospital_select_region(self, index):
        Select_Region = Select(self.driver.find_element_by_id(self.Hospitals_Region_Select_id))
        Select_Region.select_by_index(index)

    def hospital_Name(self, hospitalname):
        self.driver.find_element_by_xpath(self.Hospital_name_xpath).send_keys(hospitalname)

    def hospital_Description(self, hospitaldescription):
        self.driver.find_element_by_xpath(self.Hospital_Description_xpath).send_keys(hospitaldescription)

    def hospital_Phone(self, hospitalphone):
        self.driver.find_element_by_xpath(self.Hospital_Phone_xpath).send_keys(hospitalphone)

    def hospital_StreetAddress(self, hospitalstreetaddress):
        self.driver.find_element_by_xpath(self.Hospital_StreetAddress_xpath).send_keys(hospitalstreetaddress)

    def hospital_StreetAddress1(self, hospitalStreeAddress1):
        self.driver.find_element_by_xpath(self.Hospital1_StreetAddress_xpath).send_keys(hospitalStreeAddress1)

    def hospital_City(self, hospitalcity):
        self.driver.find_element_by_xpath(self.Hospital_City_xpath).send_keys(hospitalcity)

    def hospital_PostCode(self, hospitalPostCode):
        self.driver.find_element_by_xpath(self.Hospital_PostCode_xpath).send_keys(hospitalPostCode)

    def hospital_State(self, value):
        Select_state = Select(self.driver.find_element_by_id(self.Hospital_State_id))
        Select_state.select_by_value(value)

    def hospital_Country(self, value):
        Select_Country = Select(self.driver.find_element_by_id(self.Hospital_Country_id))
        Select_Country.select_by_value(value)

    def hospital_Submit(self, driver):
        self.driver.find_element_by_xpath(self.Hospital_Submit_Button_xpath).click()
        get_url = driver.current_url
        print(get_url)
        match_pattern = "https://dev-admin.sympliant.com/hospitals/create"
        if urlmatch(match_pattern, get_url):
            hospitalname_message = self.driver.find_element_by_xpath(self.Hospital_Already_textmessage_xpath).text
            assert hospitalname_message == "The name has already been taken."
            print(hospitalname_message)
        else:
            print("pass")