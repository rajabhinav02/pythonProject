import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='mce_0_ifr']"))
driver.find_element_by_css_selector("p").clear()
driver.find_element_by_xpath("//p").send_keys("Testing")
time.sleep(3)

driver.switch_to.default_content()
print(driver.find_element_by_css_selector("h3").text)
