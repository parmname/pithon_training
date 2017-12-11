# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLoginMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_mail(self):
        driver = self.driver
        driver.get("https://mail.ru/")
        driver.find_element_by_id("mailbox:login").click()
        driver.find_element_by_id("mailbox:login").clear()
        driver.find_element_by_id("mailbox:login").send_keys("test")
        driver.find_element_by_id("mailbox:password").click()
        driver.find_element_by_id("mailbox:password").clear()
        driver.find_element_by_id("mailbox:password").send_keys("test")
        driver.find_element_by_id("auth").submit()
        driver.find_element_by_id("mailbox:login").click()
        driver.find_element_by_id("mailbox:login").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=mailbox:login | ]]
        driver.find_element_by_id("mailbox:login").clear()
        driver.find_element_by_id("mailbox:login").send_keys("test")
        driver.find_element_by_id("mailbox:password").click()
        driver.find_element_by_id("mailbox:password").clear()
        driver.find_element_by_id("mailbox:password").send_keys("testik")
        driver.find_element_by_xpath(u"//input[@value='Войти']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
