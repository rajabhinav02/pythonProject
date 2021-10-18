from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element_by_link_text("Shop").click()
addbuttons= driver.find_elements_by_css_selector(".btn-info")

for add in addbuttons:

    name= add.find_element_by_xpath("parent::div/parent::div/div/h4").text
    if name == "Blackberry":
        add.click()

driver.find_element_by_xpath("//a[contains(@class, 'btn-primary')]").click()

name2= driver.find_element_by_xpath("//h4[@class='media-heading']/a").text

assert name2 == name

quantity=driver.find_element_by_css_selector("#exampleInputEmail1").text
print(quantity)
price= driver.find_element_by_xpath("//tr/td[3]/strong").text
print(price)
total= driver.find_element_by_xpath("//tr/td[4]/strong").text
print(total)

#assert int(quantity)*int(price)==int(total)

driver.find_element_by_css_selector(".btn-success").click()

driver.find_element_by_css_selector("#country").send_keys("IND")

wait=WebDriverWait(driver,15)

wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div/div[2]/ul/li/a")))

countries= driver.find_elements_by_xpath("//div/div[2]/ul/li/a")

for country in countries:
    if country.text == "India":
        country.click()
        break

driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_xpath("//strong").text)
assert "Success" in driver.find_element_by_xpath("//strong").text

driver.get_screenshot_as_file("Final.png")



