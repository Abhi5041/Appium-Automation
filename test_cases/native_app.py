import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_cap =dict(
    deviceName = 'Android',
    platformName = 'Android',
    appPackage='com.atoa.paywithatoadev',
    appActivity='com.atoa.paywithatoa.MainActivity'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"android.widget.Button").click()
driver.find_element(By.CLASS_NAME,"android.widget.EditText").click()
driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys('9452087226')

driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()
time.sleep(10)
driver.find_element(By.CLASS_NAME,'android.widget.EditText').send_keys('123456')
user_name =driver.find_element(By.CLASS_NAME,'android.widget.EditText')
user_name.click()
user_name.send_keys('john doe')
enter_post_code = driver.find_element(By.CLASS_NAME,'android.widget.EditText')
enter_post_code.click()
enter_post_code.send_keys()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Continue').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Skip').click()
driver.find_element(By.XPATH,'//android.widget.SeekBar[@content-desc="June"]').click()
driver.find_element(By.XPATH,'//android.widget.SeekBar[@content-desc="25"]').click()
driver.find_element(By.XPATH,'//android.widget.SeekBar[@content-desc="2002"]').click()
driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()
#creating_hashtag = driver.find_element(By.CLASS_NAME,'android.widget.EditText')
#creating_hashtag.click()
#creating_hashtag.send_keys('#Abhi')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Continue').click()
driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Continue"]').click()



