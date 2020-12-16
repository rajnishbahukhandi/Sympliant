from PomAdmin.Locators.locators import locator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class departments():
    def __init__(self, driver):
        self.driver = driver
        self.Departments_xpath = locator.Departments_xpath
        self.Departments_Create_xpath = locator.Departments_Create_xpath
        self.Departments_Hospital_id = locator.Departments_Hospital_id
        self.Departments_Name_id = locator.Departments_Name_id
        self.Departments_Description_id = locator.Departments_Description_id
        self.Departments_MainContactEmail_id = locator.Departments_MainContactEmail_id
        self.Departments_Procedures_id1 = locator.Departments_Procedures_id1
        self.Departments_Procedures_id2 = locator.Departments_Procedures_id2
        self.Departments_Submit_Button_xpath = locator.Departments_Submit_Button_xpath

    def departments_selection(self):
        self.driver.find_element_by_xpath(self.Departments_xpath).click()

    def departments_create(self, driver):
        departmentselement = self.driver.find_element_by_xpath(self.Departments_Create_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(departmentselement).click()
        actions.perform()

    def departments_hospitalId(self, hospital_id):
        Select_departmenthospital = Select(self.driver.find_element_by_id(self.Departments_Hospital_id))
        Select_departmenthospital.select_by_value(hospital_id)

    def departments_name(self, departmentname):
        self.driver.find_element_by_id(self.Departments_Name_id).send_keys(departmentname)

    def departments_description(self, departmentsdescription):
        self.driver.find_element_by_id(self.Departments_Description_id).send_keys(departmentsdescription)

    def departments_MainContactEmail(self, DepartmentsContactEmail):
        self.driver.find_element_by_id(self.Departments_MainContactEmail_id).send_keys(DepartmentsContactEmail)

    def departments_Procedures(self):
        self.driver.find_element_by_id(self.Departments_Procedures_id1).click()
        self.driver.find_element_by_id(self.Departments_Procedures_id2).click()

    def departments_Submit(self):
        self.driver.find_element_by_xpath(self.Departments_Submit_Button_xpath).click()








