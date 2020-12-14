from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from urlmatch import urlmatch
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://dev-admin.sympliant.com/")

# mason.monu@ithands.biz
# n4K3~1xZf6%4

# ray.rajnish@ithands.biz
# R@y1234

usr = input("Enter the E-Mail Address :- ")
pwd = input("Enter the Password:- ")
EnterIDNs = input("Enter the IDNs:- ")

E_MailAddress = driver.find_element_by_id('email').send_keys(usr)
Password = driver.find_element_by_id('password').send_keys(pwd)
Login = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/form/div[4]/div/button').click()

IDNs = driver.find_element_by_xpath('//*[@data-target="#menuIdn"]').click()
# Create = driver.find_element_by_xpath('//*[@id="menuIdn"]/a[2]/span').click()

# sleep(3)
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB * 2)
# sleep(1)
# actions.perform()
# for n in range(2):
#     action = actions.send_keys(Keys.TAB)
# action.double_click().perform()
sleep(3)
IDNs_Create = driver.find_element_by_xpath('//*[contains(@href,"https://dev-admin.sympliant.com/idns/create")]')
actions = ActionChains(driver)
actions.move_to_element(IDNs_Create).click()
actions.perform()

sleep(3)

Create_IDNs = driver.find_element_by_xpath("//input[@id='name']").send_keys(EnterIDNs)
description = driver.find_element_by_id("description").send_keys('user')
Button_IDN = driver.find_element_by_xpath("//button[@type='submit']").click()

get_url = driver.current_url
print(get_url)
match_pattern = "https://dev-admin.sympliant.com/idns/create"

sleep(5)
if urlmatch(match_pattern, get_url):
    Create_IDNs2 = driver.find_element_by_xpath('//*[@id="collapse-main"]/main/div/div/div/div/div[2]/form/div[1]/div/span/strong').text
    assert Create_IDNs2 == "The name has already been taken."
    print(Create_IDNs2)

else:
    print("pass")


sleep(2)
Hospitals = driver.find_element_by_xpath('//*[@data-target="#menuHospital"]').click()

sleep(2)
Hospitals_Create = driver.find_element_by_xpath('//*[contains(@href,"https://dev-admin.sympliant.com/hospitals/create")]')
actions = ActionChains(driver)
actions.move_to_element(Hospitals_Create).click()
actions.perform()

sleep(3)
Select_Idn = Select(driver.find_element_by_id("idn_id"))
Select_Idn.select_by_index(4)

Select_Region = Select(driver.find_element_by_id("region_id"))
Select_Region.select_by_index(5)

Name_Hospital = driver.find_element_by_id("name").send_keys('rajnish hospital')
Description_Hospital = driver.find_element_by_xpath("//*[@id='description']").send_keys('hospital')
Phone_Hospital = driver.find_element_by_xpath("//*[@id='phone_number']").send_keys('9898989899')
StreetAddress_Hospital = driver.find_element_by_xpath("//*[@id='street1']").send_keys('Street A-45 hospital')
StreetAddress_Hospital1 = driver.find_element_by_xpath("//*[@id='street2']").send_keys('New city A-46 hospital')
City_Hospital = driver.find_element_by_xpath("//*[@id='city']").send_keys('New City')
PostCode_Hospital = driver.find_element_by_xpath("//*[@id='post_code']").send_keys('248004')

Select_State = Select(driver.find_element_by_xpath("//*[@id='state_name']"))
Select_State.select_by_visible_text("Arizona")

Select_Country = Select(driver.find_element_by_xpath("//*[@id='country_name']"))
Select_Country.select_by_visible_text("American Samoa")

Create_HospitalBTN = driver.find_element_by_xpath("//button[@type='submit']").click()
