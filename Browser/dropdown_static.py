import select

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")



driver=webdriver.Chrome(executable_path= "C:\\ChromeDriver92\\chromedriver_win32 (5)\\chromedriver.exe", options= chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#dropdownselect= driver.find_element_by_id("dropdown-class-example").click()
#dropdowns= driver.find_elements_by_xpath("//select[@id='dropdown-class-example']/option").
dropdown=Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_visible_text("Option2")
print(dropdown.first_selected_option.get_attribute('text'))

#for dd in dropdowns:
   # dd.click()

checkboxes= driver.find_elements_by_xpath("//input[@type='checkbox']").clear()


for checkbox in checkboxes:
    if checkbox.get_attribute('name')=="checkBoxOption1":
        checkbox.click()
