import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from Base_Class import BaseClass


class NewUser(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    def launching(self):

        self.ClicK1('get_started_CLASS_NAME')
        self.ClicK1('enter_mobile_no_CLASS_NAME')
        # Mobile number screen
        self.Send_data('enter_mobile_no_CLASS_NAME',"9452087110")
        self.ClicK1('Continue_XPATH')
        time.sleep(5)
        # OTP screen
        self.Send_data('otp_CLASS_NAME','123456')
        #self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('123456')

        time.sleep(2)
        try:
            obj1 = self.select_element('connect_your_bank_ACCESSIBILITY_ID')
            if (obj1.is_displayed() == True):
                self.ClicK1('skip_ACCESSIBILITY_ID')
                #self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Skip').click()
                time.sleep(5)
                self.ClicK1('ccontinue_1_ACCESSIBILITY_ID')
                #self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Continue').click()
            else:
                print('new user')

        except:
            user_name = self.select_element('user_name_CLASS_NAME')
            #user_name = self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
            user_name.send_keys('Ashis abhi')

            self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Continue"]').click()
            # Postal Code Screen
            time.sleep(5)
            enter_post_code = self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText')
            time.sleep(2)
            enter_post_code.send_keys('WSD17')
            self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Continue"]').click()

            time.sleep(5)
            # Referral Screen Skip or Continue

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Skip').click()

            # Perform the scroll action

            touch = TouchAction(self.driver)
            touch.press(x=175, y=1001).move_to(x=175, y=1422).release().perform()
            time.sleep(2)

            self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Continue"]').click()

            time.sleep(2)  # Please confirm Atoa id
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Continue').click()
            self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Continue"]').click()

            time.sleep(3)  # Skip invite screen
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Skip').click()
            time.sleep(3)  # Skip Confrim bank screen
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Skip').click()

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Continue').click()

