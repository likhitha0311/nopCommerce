from selenium import webdriver


class LoginPage:
    textbox_username_id="Email"
    textbox_password_id = "Password"
    button_Login_xpath="//button[.='Log in']"
    link_Logout_linktext="Logout"


    def __init__(self,driver):
      self.driver=driver

    def setUserName(self,username):
      self.driver.find_element_by_id(self.textbox_username_id).clear()
      self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)


    def setPassword(self,password):
      self.driver.find_element_by_id(self.textbox_password_id).clear()
      self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def click_login(self):
     self.driver.find_element_by_xpath(self.button_Login_xpath).click()

    def click_logout(self):
     self.driver.find_element_by_link_text(self.link_Logout_linktext).click()
