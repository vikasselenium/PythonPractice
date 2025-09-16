from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #email_field= (By.ID,"email1")
    email_field_value="email1"
    #password_field=(By.XPATH, "//input[@type='password']")
    password_field_value="password1"
    #login_button=(By.XPATH,"//button[@type='submit']")
    login_button_field_value="submit-btn"
    # def enter_email(self, email):
    #     self.driver.find_element(*self.email_field).send_keys(email)
    #
    # def enter_password(self,password):
    #     self.driver.find_element(*self.password_field).send_keys(password)
    #
    # def click_on_login(self):
    #     self.driver.find_element(*self.password_field).click()

    def login_to_application(self,email,password):

        self.type_element(email,self.email_field_value,locator_type="id")
        self.type_element(password,self.password_field_value,locator_type="id")
        self.click_element(self.login_button_field_value,locator_type="class")


