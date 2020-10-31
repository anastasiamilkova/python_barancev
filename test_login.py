# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True
    
    def test_login(self):
        wd = self.wd
        wd.get("https://www.google.com/?hl=en")
        wd.find_element_by_id("gb_70").click()
        wd.find_element_by_id("identifierId").clear()
        wd.find_element_by_id("identifierId").send_keys("utestmilkova@gmail.com")
        wd.find_element_by_xpath("//div[@id='identifierNext']/div/button/div[2]").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("PasswordPython")
        wd.find_element_by_name("password").send_keys(Keys.ENTER)
        wd.find_element_by_xpath("//div[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[4]/div/span/span").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
