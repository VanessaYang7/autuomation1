#coding=utf-8
from selenium import webdriver
import unittest
from EnventXtra.Common.login import Login_event
login_url="https://app.2vanx.com/users/sign_in"

class TetsLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
      self.driver=webdriver.Firefox()
      self.driver.maximize_window()
      self.driver.get(login_url)

    @classmethod
    def tearDownClass(self):
        self.driver.refresh()
        self.driver.quit()


    def test_login(self):
        Login_event(self.driver).login("angus+qa@eventxtra.com","11111111")

    def is_login_sucess(self):
        try:
          text=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/span").text
          print text
          return  True
        except:
            return False


if __name__=="__main__":
    unittest.main()