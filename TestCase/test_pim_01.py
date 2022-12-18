from Uttlieies.readproperty import ReadConfig
from PageObject.locators import OrangeHMR
import time

class Test_PIM_01:

    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_create_pim(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        login = OrangeHMR(driver)
        login.set_username(self.username)
        login.set_password(self.password)
        login.click_login()
        time.sleep(3)
        login.click_pim()
        login.click_Add()
        login.set_details('ram','kumar')
        login.set_personal_details("afw","gwn89398","gwggw","2022-11-12",4574,5463,"2000-10-11","WDGO0800")
        save = login.saveConformation()
        time.sleep(3)
        if save == True:
            assert True
        else:
            assert False
