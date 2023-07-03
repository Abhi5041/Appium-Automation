import time

from appium import webdriver
desired_cap =dict(
    deviceName = 'Android',
    platformName = 'Android',
    browserName ='Chrome'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.get('http://google.com')
print(driver.title)
time.sleep(5)
driver.quit()