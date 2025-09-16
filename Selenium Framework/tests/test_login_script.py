
import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.webdriverfactory import WebDriverFactory
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utilities.excel_util import ExcelUtils

@pytest.mark.usefixtures("setup")
class TestLoginScenario:

    #file_path=os.path.join(os.path.dirname(__file__),"..","testdata","testdata.xlsx")
    file_path=os.path.join(os.path.dirname(__file__),"..","testdata","testdata.xlsx")
    @pytest.mark.parametrize("email,password",
                             ExcelUtils.get_excel_Data(file_path,"Sheet1"))

    def test_login(self,email,password):

        login=LoginPage(self.driver)

        login.login_to_application(email,password)

        home=HomePage(self.driver)

        wel_msg=home.get_welcome_text()

        assert "Welcome" in wel_msg,"Welcome message not found"
        home.logout_from_application()





