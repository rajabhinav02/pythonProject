from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

waiting=WebDriverWait(driver,3)

waiting.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='double-click']")))

action= ActionChains(driver)
action.context_click(driver.find_element_by_xpath("//*[@id='double-click']")).perform()
action.double_click(driver.find_element_by_css_selector("#double-click")).perform()


alertm=driver.switch_to.alert
assert "You" in alertm.text

print(alertm.text)

alertm.accept()

#action.context_click(driver.find_element_by_xpath("//*[@id='double-click']")).perform()