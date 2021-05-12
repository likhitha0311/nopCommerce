import logging
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from Utilities import XLUtils
import time


class Test_002_login_ddt:
    url = ReadConfig.getApplicationUrl()
    logger = LogGen.log_generator()
    path="./TestData/LoginData.xlsx"

    def test_login_ddt(self, setUp):
        self.driver = setUp
        self.logger.info("********Test_002_login_ddt***********")
        self.driver.get(self.url)
        self.lp = LoginPage(self.driver)
        lst_status=[]
        row=XLUtils.getRowCount(self.path,'Sheet1')

        for r in range(2,row+1):
           self.user =XLUtils.readData(self.path,'Sheet1',r,1)
           self.passwrd = XLUtils.readData(self.path, 'Sheet1',r, 2)
           self.exp=XLUtils.readData(self.path, 'Sheet1',r, 3)

           self.lp.setUserName(self.user)
           self.lp.setPassword(self.passwrd)
           self.lp.click_login()
           time.sleep(5)
           act_title = self.driver.title
           exp_title= "Dashboard / nopCommerce administration"

           if act_title == exp_title:
               if self.exp=="Pass":
                   self.logger.info("********Passed***********")
                   self.lp.click_logout();
                   lst_status.append("Pass")
               elif  self.exp=="Fail":
                   self.logger.info("********Failed***********")
                   self.lp.click_logout();
                   lst_status.append("Fail")
           elif act_title != exp_title:
               if self.exp=="Pass":
                   self.logger.info("********Failed***********")
                   #self.lp.click_logout();
                   lst_status.append("Fail")
               elif self.exp=="Fail":
                   self.logger.info("********Passed***********")
                   #self.lp.click_logout();
                   lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("********Test_002_login_ddt Passed***********")
            self.driver.close()
        else:
            self.logger.info("********Test_002_login_ddt Failed***********")
            self.driver.close()

        self.logger.info("********Completed Test_002_login_ddt ***********")




