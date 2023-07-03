import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from User_login import NewUser
from User_verification import UserVerification
from Base_Class import BaseClass
import pytest

class Testone(BaseClass):

    def test_user_login(self):
        log = self.getlogger()
        log.info("new user class is called")
        obj = NewUser(self.driver)
        obj.launching()

    def test_User_verify(self):
        log = self.getlogger()
        log.info("user verification class is called")
        obj = UserVerification(self.driver)
        obj.verifyIdentity()


