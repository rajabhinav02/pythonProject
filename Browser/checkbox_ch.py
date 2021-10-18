import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

checkboxes= driver.find_elements_by_css_selector("[type='checkbox']")

driver.implicitly_wait(3)

for ch in checkboxes:
    if ch.get_attribute('value')=='option2':
    #ch.click()

        ch.click()
        assert ch.is_selected()

radiobuttons=  driver.find_elements_by_xpath("//input[@name='radioButton']")
#radiobuttons[2].click()

for rb in radiobuttons:
    if rb.get_attribute('value')== 'radio1':
        rb.click()
        assert rb.is_selected()
validatetest = "Testing"
driver.find_element_by_css_selector("#name").send_keys("Testing")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()

alertmes=driver.switch_to.alert
print(alertmes.text)
time.sleep(3)
assert "Testing" in alertmes.text
alertmes.accept()

driver.find_element_by_css_selector("input#confirmbtn").click()

alertmessage= driver.switch_to.alert
time.sleep(2)
print(alertmessage.text)
alertmessage.dismiss()

driver.find_element_by_id("id").send_keys("hj")



driver.execute_script("window.scroll(0,-1000);")






