import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap =dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage='com.atoa.paywithatoadev',
    appActivity='com.atoa.paywithatoa.MainActivity',

)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)



def scratch_card():

    # Locate the scratch card element
    scratch_card = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.ImageView")

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
    actions = TouchAction(driver)
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

def launching():

    driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
    driver.find_element(By.CLASS_NAME,"android.widget.EditText").click()
    # Mobile number screen
    driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys('9452087110')
    driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()
    time.sleep(5)
    # OTP screen
    driver.find_element(By.CLASS_NAME,'android.widget.EditText').send_keys('123456')

    time.sleep(2)
    try:
        if(driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Connect Your Bank').is_displayed()==True):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Skip').click()
            time.sleep(5)
            driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Continue').click()
        else:
            print('new user')

    except:


        user_name =driver.find_element(By.CLASS_NAME,'android.widget.EditText')

        user_name.send_keys('Ashis abhi')
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()
        # Postal Code Screen
        time.sleep(5)
        enter_post_code = driver.find_element(By.CLASS_NAME,'android.widget.EditText')
        time.sleep(2)
        enter_post_code.send_keys('WSD17')
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()

        time.sleep(5)
        #Referral Screen Skip or Continue

        driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Skip').click()

        # Perform the scroll action

        touch = TouchAction(driver)
        touch.press(x=175, y=1001).move_to(x=175,y=1422).release().perform()
        time.sleep(2)

        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()

        time.sleep(2)            #Please confirm Atoa id
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Continue').click()
        driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()

        time.sleep(3)            # Skip invite screen
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Skip').click()
        time.sleep(3)  # Skip Confrim bank screen
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Skip').click()

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Continue').click()



def take_photo(photo_ele):
    try:
        take_photo_button =photo_ele

        take_photo_button.click()
            # Logic to capture the photo
        try:
            if (driver.find_element(By.ID,
                                        'com.android.permissioncontroller:id/permission_allow_foreground_only_button').is_displayed()):
                driver.find_element(By.ID,
                                        'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
        except:
            print('no dialog box')
        time.sleep(3)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Capture').click()
        time.sleep(3)
        # driver.find_element(AppiumBy.ACCESSIBILITY_ID,'com.motorola.camera3:id/stage1_layout').click()
        time.sleep(3)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Crop').click()
        time.sleep(3)

        print("Photo taken successfully!")


    except NoSuchElementException:

        print("Take Photo button not found!")

def verifyIdentity():
    '''click on verify'''
    time.sleep(5)
    ele = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Verify')
    #wait.until(
       #EC.presence_of_element_located(ele))
    ele.click()
    scratch_card()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Start Verification').click()
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Passport').click() #radio
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Upload Passport').click()
    time.sleep(2)
    #take_photo_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Take Photo")
    #take_photo(take_photo_button)

    def select_from_gallery():
        try:
            ''' make sure this element is present in phone'''
            gallery_item = driver.find_element(AppiumBy.XPATH,
                                               '//android.widget.LinearLayout[@content-desc="IMG_20230626_222358119.jpg, 3.29 MB, 10:23 pm"]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView')
            if gallery_item.is_displayed():
                gallery_item.click()
                driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Crop').click()
                print("Selected item from the gallery successfully!")
            else:
                print("Gallery item not found!")
        except NoSuchElementException:
            print("Gallery item not found!")
    try:
        open_gallery_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Choose from Gallery")
        if open_gallery_button.is_displayed():
            open_gallery_button.click()
            # Logic to open the gallery and navigate to the desired item
            select_from_gallery()
        else:
            print("Open Gallery button not found!")
    except NoSuchElementException:
        print("Open Gallery button not found!")



    def select_file():
        try:
            file_item = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Choose from Files")
            if file_item.is_displayed():
                file_item.click()
                print("Selected file successfully!")
            else:
                print("File item not found!")
        except NoSuchElementException:
            print("File item not found!")

    try:
        open_file_dialog_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"open_file_dialog_button")
        if open_file_dialog_button.is_displayed():
            open_file_dialog_button.click()
            # Logic to open the file selection dialog and navigate to the desired file
            select_file()
        else:
            print("Open File Dialog button not found!")
    except NoSuchElementException:
        print("Open File Dialog button not found!")


        take_selfe = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Upload a Selfie')
        take_photo(take_selfe)  # calling take_photofunction
        '''press on continue'''
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Proceed')


#def verify_details()



launching()
verifyIdentity()
#verify_details()
