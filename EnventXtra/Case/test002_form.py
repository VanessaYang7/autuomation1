#coding=utf-8
from selenium import webdriver
import unittest
import time
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
        except:
            return False

    def regi(self):
        #打开活动
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[5]/div[1]/div[2]").click()
        time.sleep(3)

    def is_regi_sucess(self):
        try:
          text=self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/span").text
          print text
        except:
            return False

    def forms(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div[5]/div[1]/div/a/span").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div[5]/div[2]/div[1]/a/span").click()
        time.sleep(3)

    def deful(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/table/tbody/tr/td[1]/a/span").click()
        time.sleep(3)

    def pron(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[4]/div[2]/form/div[1]/div/div[1]/div[2]/div/div/div/span[1]/div[3]/div[1]/div/div/span[1]").click()
        time.sleep(3)

    def maxper(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[4]/div[2]/form/div[1]/div/div[1]/div[2]/div/div/div/span[1]/div[3]/div[3]/input").sendkeys("10")
        time.sleep(3)

    def save(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/div/div/input").click()




if __name__=="__main__":
    unittest.main()