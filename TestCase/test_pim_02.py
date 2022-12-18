from Uttlieies.readproperty import ReadConfig
from PageObject.locators import OrangeHMR
import time

class Test_PIM_02:

    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_edit_pim(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        login = OrangeHMR(driver)
        login.set_username(self.username)
        login.set_password(self.password)
        login.click_login()
        time.sleep(5)
        login.click_pim()
        login.edit_emplyee("ram")
        update = login.updateConformation()
        time.sleep(3)
        if update == True:
            assert True
        else:
            assert False
