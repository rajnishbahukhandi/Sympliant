from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PomAdmin.Module.LoginModule import LoginPage
from PomAdmin.Module.ProfileLogoutModule import Profile
from PomAdmin.Module.IDNModule import IDN
from PomAdmin.Module.HospitalsModule import hospital
from PomAdmin.Module.HRegionsModule import hRegions
from PomAdmin.Module.DepartmentsModule import departments
from PomAdmin.Module.DEndoscopeModule import DEndoscope
from PomAdmin.CredentialsFile.Variable import var
import unittest
import time
# import HtmlTestRunner

class AppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get(var.URL)
        time.sleep(2)

        # Login Module function call
        loginPage = LoginPage(driver)
        loginPage.enter_username(var.username)
        loginPage.enter_password(var.password)
        loginPage.click_login(driver)

        # IDN Module function call
        idn = IDN(driver)
        idn.idn_selection()
        time.sleep(3)
        idn.idn_selection_create(driver)
        time.sleep(1)
        idn.idn_create_text(var.idnCreateText)
        idn.idn_description_text(var.idnDescriptionText)
        idn.idn_submit(driver)

        # hRegions Module function call
        time.sleep(2)
        hRegions_obj = hRegions(driver)
        hRegions_obj.hRegions_selection()
        time.sleep(2)
        hRegions_obj.hRegions_create(driver)
        time.sleep(2)
        hRegions_obj.hRegions_name(var.hRegionsName)
        hRegions_obj.hRegions_description(var.hRegionsDescription)
        hRegions_obj.hRegions_Submit(driver)

        # Hospital Module function call
        time.sleep(2)
        Hospital_Obj = hospital(driver)
        Hospital_Obj.hospital_selection()
        time.sleep(2)
        Hospital_Obj.hospital_create(driver)
        Hospital_Obj.hospital_select_Idn(var.HospitalIdn)
        Hospital_Obj.hospital_select_region(var.HospitalRegion)
        time.sleep(2)
        Hospital_Obj.hospital_Name(var.HospitalName)
        Hospital_Obj.hospital_Description(var.HospitalDescription)
        Hospital_Obj.hospital_Phone(var.HospitalPhone)
        Hospital_Obj.hospital_StreetAddress(var.HospitalStreetAddress)
        Hospital_Obj.hospital_StreetAddress1(var.HospitalStreetAddress1)
        Hospital_Obj.hospital_City(var.HospitalCity)
        Hospital_Obj.hospital_PostCode(var.HospitalPostCode)
        Hospital_Obj.hospital_State(var.HospitalState)
        Hospital_Obj.hospital_Country(var.HospitalCountry)
        Hospital_Obj.hospital_Submit(driver)

        # Departments Module function call
        time.sleep(2)
        departments_obj = departments(driver)
        departments_obj.departments_selection()
        time.sleep(2)
        departments_obj.departments_create(driver)
        departments_obj.departments_hospitalId(var.departmentsHospitalId)
        time.sleep(2)
        departments_obj.departments_name(var.departmentsName)
        departments_obj.departments_description(var.departmentsDescription)
        departments_obj.departments_MainContactEmail(var.departmentsMainContactEmail)
        departments_obj.departments_Procedures()
        departments_obj.departments_Submit()

        # DEndoscope Module function call
        time.sleep(2)
        DEndoscope_obj = DEndoscope(driver)
        DEndoscope_obj.DEndoscope_selection()
        time.sleep(2)
        DEndoscope_obj.DEndoscope_create(driver)
        DEndoscope_obj.DEndoscope_HospitalId(var.DEndoscopeHospitalId)
        DEndoscope_obj.DEndoscope_DepartmentId(var.DEndoscopeDepartmentId)
        time.sleep(2)
        DEndoscope_obj.DEndoscope_SerialNumber(var.DEndoscopeSerialNumber)
        DEndoscope_obj.DEndoscope_Description(var.DEndoscopeDescription)
        DEndoscope_obj.DEndoscope_ApproxUsage(var.DEndoscopeApproxUsage)
        DEndoscope_obj.DEndoscope_MaxUsage(var.DEndoscopeMaxUsage)
        DEndoscope_obj.DEndoscope_ServiceDate()
        time.sleep(2)
        DEndoscope_obj.DEndoscope_Active()
        DEndoscope_obj.DEndoscope_Submit_Button(driver)

        # Profile Module function call
        time.sleep(3)
        profiledashboard = Profile(driver)
        profiledashboard.click_welcome()
        profiledashboard.click_logout()

    time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/ray.rajnish/PycharmProjects/SympliantAdmin/HTMLReportsGenerates"))




