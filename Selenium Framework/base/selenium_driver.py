import logging
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
import utilities.custom_logger as cl

class SeleniumDriver:
    log = cl.customlogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    # screenshots, clickElement,typeElement, typeElement, scrolls,dragDrop, waits
    # standard methods we can keep here
    # we will keep utility folfer specific to logger functionality

    def take_screenshot(self):
        try:
            cwd=os.getcwd()
            screenshot_dir=os.path.join(os.getcwd(),"screenshots")
            timestamp= datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file_path=screenshot_dir+"\\"+"automation"+"_"+timestamp+".png"
            #file_path=os.path.join(screenshot_dir+"automation",timestamp,".png")
            status= self.driver.save_screenshot(file_path)
            #status= self.driver.save_screenshot(file_path)
            return file_path

        except Exception as e:
            print(f"cound not take screenshot {e}")
            return None

    def get_by_type(self, locator_type):
        locator_type=locator_type.lower()

        if locator_type=="id":
            return By.ID

        elif locator_type=="name":
            return By.NAME
        elif locator_type=="class":
            return By.CLASS_NAME
        elif locator_type=="xpath":
            return By.XPATH
        elif locator_type=="CSS":
            return By.CSS_SELECTOR
        elif locator_type=="link":
            return By.LINK_TEXT
        elif locator_type=="partial_link":
            return By.PARTIAL_LINK_TEXT
        elif locator_type=="tag":
            return By.TAG_NAME
        else:
            #print("Locator type "+locator_type+" not supported")
            self.log.info("Locator type "+locator_type+" not supported")
            return None

    def get_element(self,locator,locator_type='id'):
        element=None
        try:
            locator_type=locator_type.lower()
            by_type=self.get_by_type(locator_type)
            element=self.driver.find_element(by_type,locator)
            #print("Element found")
            self.log.info("Element found using "+locator_type+" with value"+locator)

        except Exception as e:
            #print("Element not found", e)
            self.log.info("Element not found using " + locator_type + " with value" + locator)

        return element

    def click_element(self, locator,locator_type):
        try:
            element= self.get_element(locator,locator_type)
            element.click()
            print("Click on element")
            self.log("clicked on element " +locator)
        except Exception as e:
            print("Can not click on element ",e)

    def type_element(self,data, locator,locator_type="id"):
        try:
            element=self.get_element(locator,locator_type)
            element.send_keys(data)
            print("Clicked on element")
            self.log("clicked on element " + locator)
        except Exception as e:
            print("can not click on element",e)

    def explict_wait(self, locator, locator_type='id', timeout=30,pollfrequency=1):
        element=None
        try:
            by_type=self.get_by_type(locator)
            wait=WebDriverWait(self.driver,timeout,
                               poll_frequency=1,
                               ignored_exceptions=[NoSuchElementException,
                                                   StaleElementReferenceException,
                                                   ElementNotInteractableException,
                                                   ElementNotVisibleException])

            element= wait.until(expected_conditions.element_to_be_clickable(by_type))
            print("Element found with explict wait")
            self.log("Element found--> " + locator)

        except Exception as e:
            print("Element not found, e")

        return element



