from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PomAdmin.Module.LoginModule import LoginPage
from PomAdmin.CredentialsFile.Variable import var
import unittest
import time

class LoginTestCase(unittest.TestCase):
    # by default, python unittest executes testcases in alphabetical order.

    @classmethod
    def setUpClass(cls):
        # setUpClass method will be executed before running any test method.
        # setUpClass method gets executed once per test class.
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_loginOfInvalidEMailAddress(self):
        driver = self.driver
        driver.get(var.URL)
        time.sleep(2)
        loginInvalidEmail = LoginPage(driver)
        loginInvalidEmail.enter_username(var.invalidUsername)
        loginInvalidEmail.enter_password(var.password)
        loginInvalidEmail.click_login(driver)

    def test_loginOfInvalidPassword(self):
        driver = self.driver
        driver.get(var.URL)
        time.sleep(2)
        loginInvalidPassword = LoginPage(driver)
        loginInvalidPassword.enter_username(var.username)
        loginInvalidPassword.enter_password(var.invalidPassword)
        loginInvalidPassword.click_login(driver)

    def test_loginOfNullCredentials(self):
        driver = self.driver
        driver.get(var.URL)
        time.sleep(2)
        loginNullCredentials = LoginPage(driver)
        loginNullCredentials.click_loginalert(driver)

    def test_loginOfValidCredentials(self):
        driver = self.driver
        driver.get(var.URL)
        time.sleep(2)
        loginValidCredentials = LoginPage(driver)
        loginValidCredentials.enter_username(var.username)
        loginValidCredentials.enter_password(var.password)
        loginValidCredentials.click_login(driver)

    time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # tearDownClass method will be executed after completing all the test methods and all in a class.
        # tearDownClass method will be executed only once in the python unittest.
        cls.driver.close()