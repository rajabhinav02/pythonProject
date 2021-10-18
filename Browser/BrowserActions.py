import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


waiting=WebDriverWait(driver,5)

waiting.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1")))

action= ActionChains(driver)

action.move_to_element(driver.find_element_by_css_selector("#mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()

driver.find_element_by_css_selector("#show-textbox").click()
assert driver.find_element_by_css_selector("#displayed-text").is_displayed()

driver.find_element_by_xpath("//input[@id='displayed-text']").send_keys("New")

time.sleep(5)

driver.find_element_by_xpath("//*[@id='hide-textbox']").click()

assert not driver.find_element_by_xpath("//*[@id='displayed-text']").is_displayed()
