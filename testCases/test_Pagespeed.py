from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Utilities import XLUtils
import time


class Test_PageSpeed:
    path=".//TestData/PageSpeed.xlsx"
    options=webdriver.ChromeOptions()
    options.headless= True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def test_PageSpeed(self):
        row=XLUtils.getRowCount(self.path,"Pagespeed")


        for r in range(2, row+1):
            time.sleep(2)
            url=XLUtils.readData(self.path,"Pagespeed",r,1)
            file_name_mobile=XLUtils.readData(self.path,"Pagespeed",r,2)
            file_name_desktop = XLUtils.readData(self.path, "Pagespeed", r, 3)
            self.driver.get(url)
            wait=WebDriverWait(self.driver,40)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[.='Mobile']"))).click()
            time.sleep(2)
            data=self.driver.find_element_by_xpath("(//div[@class='lh-gauge__percentage'])[1]").text
            time.sleep(1)
            XLUtils.writeData(self.path, "Pagespeed", r, 4, data)
            #self.driver.save_screenshot(".//Screenshots//"+file_name_mobile+".png")

            S =lambda X:self.driver.execute_script("return document.body.parentNode.scroll"+X)
            self.driver.set_window_size(S('Width'), S('Height'))
            self.driver.find_element_by_tag_name("body").screenshot(".//Screenshots//"+file_name_mobile+".png")

            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[.='Desktop']"))).click()
            time.sleep(2)
            data1 = self.driver.find_element_by_xpath("(//div[@class='lh-gauge__percentage'])[2]").text
            time.sleep(1)
            XLUtils.writeData(self.path, "Pagespeed", r, 5,data1)
            self.driver.find_element_by_tag_name("body").screenshot(".//Screenshots//" + file_name_desktop+".png")



