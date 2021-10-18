import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\\ChromeDriver92\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


#driver.find_element(By.CSS_SELECTOR,"#hrefIncChd").click()
for i in range(1,4):
    driver.find_element_by_css_selector(".paxinfo").click()
    wait = WebDriverWait(driver,10)
    wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"#hrefIncChd"))).click()
    driver.find_element_by_id("btnclosepaxoption").click()
#print(driver.find_element_by_css_selector(".paxinfo").get_attribute('value'))

print(driver.find_element_by_css_selector(".paxinfo").get_attribute("text"))

time.sleep(5)
driver.quit()