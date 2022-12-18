import time

from selenium.webdriver.common.by import By


class OrangeHMR:
    #loginpage
    txt_username_name = "username"
    txt_password_name = "password"
    btn_login_name = "//button[@type='submit']"
    #pim
    btn_pim_xpath = "//span[normalize-space()='PIM']"
    #add empo
    btn_add_xpath = "//button[normalize-space()='Add']"
    txt_firstname_name = "firstName"
    txt_lastname_name = "lastName"
    btn_save_xpath = "//button[normalize-space()='Save']"
    txt_success_xpath = "//p[text()='Success']"
    # person details
    txt_nickname_xpath = "//form[@class='oxd-form']/div[1]//input[@class='oxd-input oxd-input--active']"
    txt_otherid_xpath = "//form[@class='oxd-form']/div[2]/div[1]/div[2]//input[@class='oxd-input oxd-input--active']"
    txt_drivinglicens_xpath = "//div[2]/div[2]/div[1]/div/div[2]/input[@class='oxd-input oxd-input--active']"
    txt_expdate_xpath = "//form[@class='oxd-form']/div[2]/div[2]/div[2]//input[@class='oxd-input oxd-input--active']"
    txt_ssnnumber_xpath = "//form[@class='oxd-form']/div[2]/div[3]/div[1]//input[@class='oxd-input oxd-input--active']"
    txt_sinnumber_xpath = "//form[@class='oxd-form']/div[2]/div[3]/div[2]//input[@class='oxd-input oxd-input--active']"
    btn_nationality_xpath = "//form[@class='oxd-form']/div[3]/div[1]/div[1]//i"
    btn_select_nationality_xpath = "//*[contains(text(),'Indian')]"
    btn_maritalstatus_xpath = "//form[@class='oxd-form']/div[3]/div[1]/div[2]//i"
    btn_select_maritialstatus_xpath = "//*[contains(text(),'Single')]"

    txt_dob_xpath = "//form[@class='oxd-form']/div[3]/div[2]/div[1]//input[@class='oxd-input oxd-input--active']"
    btn_male_xpath = "//label[normalize-space()='Male']"
    txt_militaryservice_xpath = "//div[4]//div[2]/input[@class='oxd-input oxd-input--active']"
    btn_personsave_xpath = "//form/div[5]//button[@type='submit']"
    btn_bloodtype_xpath = "//div[@class='orangehrm-custom-fields']//i"
    btn_select_bloodtype_xpath = "//*[contains(text(),'A+')]"
    btn_customfieldsave_xpath = "//form/div[2]//button[@type='submit']"


    # edit
    txt_employename_xpath = "//div[1]/div/div[2]/div/div/input[@placeholder='Type for hints...']"
    drp_employeename_xpath = "//*[contains(text(),'ram')]"
    btn_search_xpath = "//button[@type='submit']"
    btn_edit_xpath = "//button/i[@class ='oxd-icon bi-pencil-fill']"
    btn_select_maritialstatus_edit_xpath = "//*[contains(text(),'Married')]"

    # delete
    btn_delete_xpath = "//button/i[@class='oxd-icon bi-trash']"
    btn_conformdelete_xpath = "//div[3]/button[2]"




    def __init__(self, driver):
        self.driver = driver

    def set_username(self, name):
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(name)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_name).click()

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.btn_pim_xpath).click()

    def click_Add(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def set_details(self,firstname,lastname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()


    def set_personal_details(self,nickname, otherid,licence,date,sin,ssn,dob,militaryservice):
        self.driver.find_element(By.XPATH, self.txt_nickname_xpath).send_keys(nickname)
        self.driver.find_element(By.XPATH, self.txt_otherid_xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH, self.txt_drivinglicens_xpath).send_keys(licence)
        self.driver.find_element(By.XPATH, self.txt_expdate_xpath).send_keys(date)
        self.driver.find_element(By.XPATH, self.txt_sinnumber_xpath).send_keys(sin)
        self.driver.find_element(By.XPATH, self.txt_ssnnumber_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH, self.btn_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_select_nationality_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_maritalstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_select_maritialstatus_xpath).click()

        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_male_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_militaryservice_xpath).send_keys(militaryservice)
        self.driver.find_element(By.XPATH, self.btn_personsave_xpath).click()

        self.driver.find_element(By.XPATH, self.btn_bloodtype_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_select_bloodtype_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_customfieldsave_xpath).click()

    def edit_emplyee(self, empname):
        self.driver.find_element(By.XPATH, self.txt_employename_xpath).send_keys(empname)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drp_employeename_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_edit_xpath).click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_maritalstatus_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_select_maritialstatus_edit_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_personsave_xpath).click()

    def delete_employee(self,empname):
        self.driver.find_element(By.XPATH, self.txt_employename_xpath).send_keys(empname)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.drp_employeename_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_delete_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_conformdelete_xpath).click()

    txt_save_mes_xpath = "//*[text()='Successfully Saved']"
    txt_update_mes_xpath = "//*[text()='Successfully Updated']"
    txt_delete_mes_xpath = "//*[text()='Successfully Deleted']"

    def saveConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_save_mes_xpath).is_displayed()
        except:
            return False

    def updateConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_update_mes_xpath).is_displayed()
        except:
            return False

    def deleteConformation(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_delete_mes_xpath).is_displayed()
        except:
            return False
