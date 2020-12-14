from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from PomAdmin.Pages.LoginPage import LoginPaget
from PomAdmin.Pages.Profilelogout import Profile
from PomAdmin.Pages.IDNPage import IDN
from PomAdmin.Pages.HospitalsPage import hospital
from PomAdmin.Pages.HRegionsPage import hRegions
from PomAdmin.Pages.DepartmentsModule import departments
from PomAdmin.Pages.DEndoscopeModule import DEndoscope
# import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://dev-admin.sympliant.com/")
        time.sleep(2)

        # Login Module function call
        loginPage = LoginPaget(driver)
        loginPage.enter_username("ray.rajnish@ithands.biz")
        loginPage.enter_password("R@y1234")
        loginPage.click_login()

        # IDN Module function call
        idn = IDN(driver)
        idn.idn_selection()
        time.sleep(3)
        idn.idn_selection_create(driver)
        time.sleep(1)
        idn.idn_create_text("rahul02")
        idn.idn_description_text("creating description")
        idn.idn_submit(driver)

        # hRegions Module function call
        time.sleep(2)
        hRegions_obj = hRegions(driver)
        hRegions_obj.hRegions_selection()
        time.sleep(2)
        hRegions_obj.hRegions_create(driver)
        time.sleep(2)
        hRegions_obj.hRegions_name('ray region')
        hRegions_obj.hRegions_description('hregions hospital')
        hRegions_obj.hRegions_Submit(driver)


        # Hospital Module function call
        time.sleep(2)
        Hospital_Obj = hospital(driver)
        Hospital_Obj.hospital_selection()
        time.sleep(2)
        Hospital_Obj.hospital_create(driver)
        Hospital_Obj.hospital_select_Idn(4)
        Hospital_Obj.hospital_select_region(3)
        time.sleep(2)
        Hospital_Obj.hospital_Name("rajnish hospital")
        Hospital_Obj.hospital_Description('hospital')
        Hospital_Obj.hospital_Phone('9898989899')
        Hospital_Obj.hospital_StreetAddress('Street A-45 hospital')
        Hospital_Obj.hospital_StreetAddress1('New city A-46 hospital')
        Hospital_Obj.hospital_City('New City')
        Hospital_Obj.hospital_PostCode('248004')
        Hospital_Obj.hospital_State("California")
        Hospital_Obj.hospital_Country("France")
        Hospital_Obj.hospital_Submit(driver)


        # Departments Module function call
        departments_obj = departments(driver)
        departments_obj.departments_selection()
        time.sleep(2)
        departments_obj.departments_create(driver)
        departments_obj.departments_hospitalId("24")
        time.sleep(2)
        departments_obj.departments_name('departments rajnish')
        departments_obj.departments_description('departments of hospitals')
        departments_obj.departments_MainContactEmail('rajnishbahukhandi@gmail.com')
        departments_obj.departments_Procedures()
        departments_obj.departments_Submit()

        # DEndoscope Module function call
        DEndoscope_obj = DEndoscope(driver)
        DEndoscope_obj.DEndoscope_selection()
        time.sleep(2)
        DEndoscope_obj.DEndoscope_create(driver)
        DEndoscope_obj.DEndoscope_HospitalId("39")
        DEndoscope_obj.DEndoscope_DepartmentId("136")
        time.sleep(2)
        DEndoscope_obj.DEndoscope_SerialNumber('45633')
        DEndoscope_obj.DEndoscope_Description('DEndoscope Description testing')
        DEndoscope_obj.DEndoscope_ApproxUsage('2')
        DEndoscope_obj.DEndoscope_MaxUsage('4')
        DEndoscope_obj.DEndoscope_ServiceDate()







        # Profile function call
        # time.sleep(2)
        # profiledashboard = Profile(driver)
        # profiledashboard.click_welcome()
        # profiledashboard.click_logout()

    #     time.sleep(3)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()



# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/ray.rajnish/PycharmProjects/SympliantAdmin/HTMLReportsGenerates"))




