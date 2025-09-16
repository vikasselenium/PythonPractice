from selenium import webdriver
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):

    welcome_field=(By.CLASS_NAME,"welcomeMessage")
    welcome_field="welcomeMessage"
    side_menu= "//img[@alt='menu']"
    log_out_field="//button[normalize-space()='Sign out']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def get_welcome_text(self, welcome_field=None):
       return self.get_element(self.welcome_field,"class").text
       #return self.driver.find_element(*self.welcome_field).text

    def logout_from_application(self):
        self.click_element(self.side_menu,locator_type="xpath")
        self.click_element(self.log_out_field,locator_type='xpath')