from Uttlieies.readproperty import ReadConfig
from PageObject.locators import OrangeHMR
import time

class Test_Login_01:

    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_valid_login(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        login = OrangeHMR(driver)
        login.set_username(self.username)
        login.set_password(self.password)
        login.click_login()
        time.sleep(5)
