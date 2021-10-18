import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\ChromeDriver92\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("IN")
time.sleep(3)

countries= driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")


print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

name= driver.find_element_by_css_selector("#autosuggest").get_attribute('value')
print(name)

assert (name=="India")