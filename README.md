# Sympliant
Sympliant Healthcare Admin script in python.

POM(Page Object Module) based script using the Python.

PomAdmin is the main folder. It consists of the child folder of Module, Locators, CredentialsFile, TestCase.
Module is consists of all the modules of the Sympliant Application of Admin.
Locators consist of the different locator (using:- id,xpath) for all modules.
Credentials file are consist of the variable, URL, Credentials.
TestCase consists of the different test cases including the negative with positive test case of login and the flow of the application.



Automated testing with Headless Chrome. Headless Chrome (as opposed to testing directly in Node) is that your JavaScript tests will be executed in the same environment as users of your site. Headless Chrome gives you a real browser context without the memory overhead of running a full version of Chrome.

options = webdriver.ChromeOptions()

options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)



Take screenshots used the PyAutoGUI. 

pip3 install pyautogui

PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications. The API is designed to be as simple. PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.

Method written in the TakeScreenshot/CaptureScreen.py

All the screenshot stored in TakeScreenshot/UpdateScreenshots
