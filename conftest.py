import pytest
from appium import webdriver

from Utilites.configReader import readConfig


@pytest.fixture(scope='class')
def setup(request):
    desired_cap = dict(
        deviceName = readConfig("basic info",'deviceName'),
        platformName=readConfig("basic info",'platformName'),
        appPackage=readConfig("basic info",'appPackage'),
        appActivity=readConfig("basic info",'appActivity'),
    )
    driver = webdriver.Remote(readConfig("basic info",'url'), desired_cap)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()