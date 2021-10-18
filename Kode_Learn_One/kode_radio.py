from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
base_url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(base_url)
#driver.find_element_by_xpath("//input[@id='bmwcheck']").click()

chbs= driver.find_elements_by_css_selector("[type='checkbox']")

for cb in chbs:
    cb.click()

rbs = driver.find_elements_by_css_selector("[type='radio']")

for r in rbs:
    if r.get_attribute('value')=='radio1':
        r.click()