import time

from selenium import webdriver

driver=webdriver.Chrome()
#driver=webdriver.Edge()
#driver=webdriver.Firefox()
time.sleep(5)
print(driver)
print(type(driver))
#driver.close()

#webdriver commands
#Navigation panels

#driver.get("https://www.google.com")
driver.get("https://www.selenium.dev/")
print(f"title is=> {driver.title}")
print(f"current URL=>{driver.current_url}")
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.save_screenshot("screenshot.png")
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.refresh()
time.sleep(3)

driver.quit()

