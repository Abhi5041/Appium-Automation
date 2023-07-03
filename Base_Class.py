import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from Utilites.configReader import readConfig

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggername= inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def ClicK1(self,key,locator ='locator'):
        if str(key).endswith("_ACESSIABILITYID"):
            self.driver.find_element(By.CSS_SELECTOR,readConfig(locator,key)).click()
        elif str(key).endswith("_XPATH"):
            self.driver.find_element(By.XPATH,readConfig(locator,key)).click()
        elif str(key).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME,readConfig(locator,key)).click()

    def Send_data(self,key,data,locator ='locator'):
        if str(key).endswith("_ACESSIABILITYID"):
            self.driver.find_element(By.CSS_SELECTOR,readConfig(locator,key)).send_keys(data)
        elif str(key).endswith("_XPATH"):
            self.driver.find_element(By.XPATH,readConfig(locator,key)).send_keys(data)
        elif str(key).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME,readConfig(locator,key)).send_keys(data)

    def grab_text(self,key,locator ='locator'):
        if str(key).endswith("_ACESSIABILITYID"):
            self.driver.find_element(By.CSS_SELECTOR,readConfig(locator,key)).click()
        elif str(key).endswith("_XPATH"):
            self.driver.find_element(By.XPATH,readConfig(locator,key)).click()
        elif str(key).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME,readConfig(locator,key)).click()

    def select_element(self,key,locator ='locator'):
        if str(key).endswith("_ACESSIABILITYID"):
            ele = self.driver.find_element(By.CSS_SELECTOR,readConfig(locator,key)).click()
        elif str(key).endswith("_XPATH"):
            ele = self.driver.find_element(By.XPATH,readConfig(locator,key)).click()
        elif str(key).endswith("_CLASS_NAME"):
            ele = self.driver.find_element(By.CLASS_NAME,readConfig(locator,key)).click()
        return ele