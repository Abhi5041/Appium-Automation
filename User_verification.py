import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException

from Base_Class import BaseClass


class UserVerification(BaseClass):
    def __init__(self,driver):
        self.driver = driver

    def scratch_card(self):

        # Locate the scratch card element
        scratch_card = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")

        # Get the dimensions of the scratch card element
        card_location = scratch_card.location
        card_size = scratch_card.size
        card_width = card_size["width"]
        card_height = card_size["height"]

        # Calculate the start and end points for scratching
        start_x = card_location["x"] + int(card_width * 0.2)
        end_x = card_location["x"] + int(card_width * 0.8)
        start_y = card_location["y"] + int(card_height * 0.5)
        end_y = start_y

        # Perform the scratch action using touch gestures
        actions = TouchAction(self.driver)
        actions.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()
        time.sleep(6)
        # try:
        #     revealed_content = driver.find_element_by_id("revealed_content")
        #     if revealed_content.is_displayed():
        #         print("Scratch card revealed:", revealed_content.text)
        #     else:
        #         print("Failed to reveal scratch card content")
        # except NoSuchElementException:
        #     print("Failed to find revealed content element")

    def take_photo(self,photo_ele):
        try:
            take_photo_button = photo_ele

            take_photo_button.click()
            # Logic to capture the photo
            try:
                if (self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                        'com.android.permissioncontroller:id/permission_allow_foreground_only_button').is_displayed()):
                    self.ClicK1("permissiion_ACCESSIBILITY_ID")
            except:
                print('no dialog box')
            time.sleep(3)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Capture').click()
            time.sleep(3)
            # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'com.motorola.camera3:id/stage1_layout').click()
            time.sleep(3)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Crop').click()
            time.sleep(3)

            print("Photo taken successfully!")


        except NoSuchElementException:

            print("Take Photo button not found!")

    def select_from_gallery(self):
        try:
            ''' make sure this element is present in phone'''
            gallery_item = self.driver.find_element(AppiumBy.XPATH,
                                               '//android.widget.LinearLayout[@content-desc="IMG_20230626_222358119.jpg, 3.29 MB, 10:23 pm"]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView')
            if gallery_item.is_displayed():
                gallery_item.click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Crop').click()
                print("Selected item from the gallery successfully!")
            else:
                print("Gallery item not found!")
        except NoSuchElementException:
            print("Gallery item not found!")



    def select_file(self):
        try:
            file_item = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Choose from Files")
            if file_item.is_displayed():
                file_item.click()
                print("Selected file successfully!")
            else:
                print("File item not found!")
        except NoSuchElementException:
            print("File item not found!")



    def verifyIdentity(self):
        '''click on verify'''
        time.sleep(5)
        ele = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Verify')
        # wait.until(
        # EC.presence_of_element_located(ele))
        ele.click()
        self.scratch_card()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Start Verification').click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Passport').click()  # radio
        time.sleep(2)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Passport').click()
        time.sleep(2)
        try:

            take_photo_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Take Photo")
            self.take_photo(take_photo_button)
        except NoSuchElementException:
            print("take photo button not found!")

        try:
            open_gallery_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Choose from Gallery")
            if open_gallery_button.is_displayed():
                open_gallery_button.click()
                # Logic to open the gallery and navigate to the desired item
                self.select_from_gallery()
            else:
                print("Open Gallery button not found!")
        except NoSuchElementException:
            print("Open Gallery button not found!")

        try:
            open_file_dialog_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "open_file_dialog_button")
            if open_file_dialog_button.is_displayed():
                open_file_dialog_button.click()
            # Logic to open the file selection dialog and navigate to the desired file
                self.select_file()
            else:
                print("Open File Dialog button not found!")
        except NoSuchElementException:
            print("Open File Dialog button not found!")


        take_selfe = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload a Selfie')
        self.take_photo(take_selfe)  # calling take_photofunction
            #  '''press on continue'''
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Proceed')