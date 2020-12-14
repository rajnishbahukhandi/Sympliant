class locator():

    # LoginPage Elements
    eMailAddress_textbox_id = 'email'
    password_textbox_id = "password"
    login_button_xpath = "/html/body/div/div[2]/div[3]/div/div/form/div[4]/div/button"

    # Profile objects
    welcome_Profile_link_id = "navbarDropdown"
    logoutProfile_xpath = '//*[contains(@href,"https://dev-admin.sympliant.com/logout")]'

    # IDN Elements
    IDN_Button_xpath = '//*[@data-target="#menuIdn"]'
    IDN_Create_Button_xpath = '//*[contains(@href,"https://dev-admin.sympliant.com/idns/create")]'
    IDN_Create_Textbox_xpath = "//input[@id='name']"
    IDN_Create_description_Textbox_id = "description"
    IDN_Submit_Button_xpath = "//button[@type='submit']"
    IDN_Already_textmessage_xpath = '//*[@id="collapse-main"]/main/div/div/div/div/div[2]/form/div[1]/div/span/strong'

    # HRegions Elements
    hRegions_xpath = '//*[@data-target="#menuRegion"]'
    hRegions_Create_xpath = '//*[contains(@href,"https://dev-admin.sympliant.com/regions/create")]'
    hRegions_name_id = 'name'
    hRegions_description_id = 'description'
    hRegions_Submit_Button_xpath = '//button[@type="submit"]'
    hRegions_Already_textmessage_xpath = '//*[@id="collapse-main"]/main/div/div/div/div/div[2]/form/div[1]/div/span/strong'

    # Hospital Elements
    Hospital_xpath = '//*[@data-target="#menuHospital"]'
    Hospitals_Create_xpath = '//*[contains(@href,"https://dev-admin.sympliant.com/hospitals/create")]'
    Hospitals_Idn_Select_Id = "idn_id"
    Hospitals_Region_Select_id = "region_id"
    Hospital_name_xpath = '//*[@placeholder="Name"]'
    Hospital_Description_xpath = "//*[@id='description']"
    Hospital_Phone_xpath = "//*[@id='phone_number']"
    Hospital_StreetAddress_xpath = "//*[@id='street1']"
    Hospital1_StreetAddress_xpath = "//*[@id='street2']"
    Hospital_City_xpath = "//*[@id='city']"
    Hospital_PostCode_xpath = "//*[@id='post_code']"
    Hospital_State_id = "state_name"
    Hospital_Country_id = "country_name"
    Hospital_Submit_Button_xpath = '//button[@type="submit"]'
    Hospital_Already_textmessage_xpath = '//*[@id="collapse-main"]/main/div/div/div/div/div[2]/form/div[3]/div/span/strong'

    # Departments Elements
    Departments_xpath = '//*[@data-target="#menuDepartment"]'
    Departments_Create_xpath = '//*[contains(@href,"https://dev-admin.sympliant.com/departments/create")]'
    Departments_Hospital_id = 'hospital_id'
    Departments_Name_id = "name"
    Departments_Description_id = 'description'
    Departments_MainContactEmail_id = 'main_contact_email'
    Departments_Procedures_id1 = 'defaultCheck14'
    Departments_Procedures_id2 = 'defaultCheck17'
    Departments_Submit_Button_xpath = '//button[@type="submit"]'

    # DEndoscope Elements
    DEndoscope_xpath = '//*[@data-target="#menuDepartmentEndoscope"]'
    DEndoscope_create_xpath = '//*[contains(@href,"https://dev-admin.sympliant.com/department-endoscopes/create")]'
    DEndoscope_Hospital_id = 'hospital_id'
    DEndoscope_Department_id = 'department_id'
    DEndoscope_Endoscope_id = 'endoscope_id'
    DEndoscope_SerialNumber_id = 'serial_number'
    DEndoscope_Description_id = 'description'
    DEndoscope_ApproxUsage_id = 'approx_usage'
    DEndoscope_MaxUsage_id = 'max_usage'
    DEndoscope_ServiceDate_xpath = '//*[@name="service_initiated_at"]'

