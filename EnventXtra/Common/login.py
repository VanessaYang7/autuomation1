#coding=utf-8
from selenium import webdriver
import unittest
import time



class Login_event(unittest.TestCase):

   def __init__(self,driver):
       self.driver=driver


   def input_email(self,email):
        #输入登录邮箱账号
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/div[2]/div[1]/input").clear()
        self.driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/div[2]/div[1]/input").send_keys(email)
        time.sleep(3)

   def click_button(self):
       self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div[3]/button").click()
       time.sleep(3)
   def input_psw(self,psw):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div[2]/form/div[2]/div/input").clear()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div[2]/form/div[2]/div/input").send_keys(psw)
        time.sleep(3)

   def sumbmit(self):
       self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div[2]/form/div[4]/button").click()

   def login(self,email,psw):
        self.input_email(email)
        self.click_button()
        self.input_psw(psw)
        self.sumbmit()