import logging
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import pytest
from pageObjects.LoginPage import LoginPage




class Test_001_login:
    url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.log_generator()

    def test_homepagetitle(self,setUp):
        self.logger.info("********Test_001_login:test_homepagetitle***********")
        self.driver=setUp()
        self.driver.get(self.url)
        actual_title=self.driver.title

        if actual_title == "Your store. Login":
            self.logger.info("******Title verified*******")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.logger.error("******Title failed*******")
            self.driver.close()
            assert False


    def test_login(self,setUp):
        self.driver = setUp
        self.logger.info("********Test_001_login:test_login***********")
        self.driver.get(self.url)
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.click_login()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.logger.info("******Login passed*******")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/test_login.png")
            self.logger.error("******Login failed*******")
            self.driver.close()
            assert False



