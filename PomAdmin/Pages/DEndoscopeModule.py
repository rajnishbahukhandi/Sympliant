from PomAdmin.Locators.locators import locator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class DEndoscope():
    def __init__(self, driver):
        self.driver = driver
        self.DEndoscope_xpath = locator.DEndoscope_xpath
        self.DEndoscope_create_xpath = locator.DEndoscope_create_xpath
        self.DEndoscope_Hospital_id = locator.DEndoscope_Hospital_id
        self.DEndoscope_Department_id = locator.DEndoscope_Department_id
        self.DEndoscope_Endoscope_id = locator.DEndoscope_Endoscope_id
        self.DEndoscope_SerialNumber_id = locator.DEndoscope_SerialNumber_id
        self.DEndoscope_Description_id = locator.DEndoscope_Description_id
        self.DEndoscope_ApproxUsage_id = locator.DEndoscope_ApproxUsage_id
        self.DEndoscope_MaxUsage_id = locator.DEndoscope_MaxUsage_id
        self.DEndoscope_ServiceDate_xpath = locator.DEndoscope_ServiceDate_xpath

    def DEndoscope_selection(self):
        self.driver.find_element_by_xpath(self.DEndoscope_xpath).click()

    def DEndoscope_create(self, driver):
        DEndoscopeElement = self.driver.find_element_by_xpath(self.DEndoscope_create_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(DEndoscopeElement).click()
        actions.perform()

    def DEndoscope_HospitalId(self, DEndoscopeHospitalId):
        Select_DEndoscopeHospitalID = Select(self.driver.find_element_by_id(self.DEndoscope_Hospital_id))
        Select_DEndoscopeHospitalID.select_by_value(DEndoscopeHospitalId)

    def DEndoscope_DepartmentId(self, DEndoscopeDepartmentId):
        Select_DEndoscopeDepartmentId = Select(self.driver.find_element_by_id(self.DEndoscope_Department_id))
        Select_DEndoscopeDepartmentId.select_by_value(DEndoscopeDepartmentId)

    def DEndoscope_EndoscopeId(self,DEndoscopeEndoscopeId):
        Select_DEndoscopeEndoscopeId = Select(self.driver.find_element_by_id(self.DEndoscope_Endoscope_id))
        Select_DEndoscopeEndoscopeId.select_by_value(DEndoscopeEndoscopeId)

    def DEndoscope_SerialNumber(self, DEndoscopeSerialNumber):
        self.driver.find_element_by_id(self.DEndoscope_SerialNumber_id).send_keys(DEndoscopeSerialNumber)

    def DEndoscope_Description(self, DEndoscopeDescription):
        self.driver.find_element_by_id(self.DEndoscope_Description_id).send_keys(DEndoscopeDescription)

    def DEndoscope_ApproxUsage(self, DEndoscopeApproxUsage):
        self.driver.find_element_by_id(self.DEndoscope_ApproxUsage_id).send_keys(DEndoscopeApproxUsage)

    def DEndoscope_MaxUsage(self, DEndoscopeMaxUsage):
        self.driver.find_element_by_id(self.DEndoscope_MaxUsage_id).send_keys(DEndoscopeMaxUsage)

    def DEndoscope_ServiceDate(self):
        self.driver.find_element_by_xpath(self.DEndoscope_ServiceDate_xpath).click()


