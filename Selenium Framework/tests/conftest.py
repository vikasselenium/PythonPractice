import allure
import pytest

from base.webdriverfactory import WebDriverFactory
from base.selenium_driver import SeleniumDriver

@pytest.fixture(scope='class')
def setup(request):
    wdf = WebDriverFactory("edge")
    driver = wdf.getWebDriverInstance()
    print("application is up and running")
    if request.cls is not None:
        request.cls.driver=driver

    yield driver
    driver.quit()
    print("Closing the browser")


@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    print("Executing PyTest Hooks")
    outcome=yield
    report= outcome.get_result()
    print("Captured result")

    if report.when=="call" and (report.failed or report.outcome=="broken"):
        print("Attaching screenshots to report on failure")
        if hasattr(item.instance,"driver"):
            driver=item.instance.driver
            selenium_driver=SeleniumDriver(driver)
            screenshot_path=selenium_driver.take_screenshot()
            print(screenshot_path)
            with allure.step("Attach Screenshot on Failure/Broken"):
                allure.attach.file(screenshot_path,name="Failure Screenshot",
                                  attachment_type=allure.attachment_type.PNG)
            # with  allure.step("Exception details"):
            #     allure.attach(str(call,excinfo))



