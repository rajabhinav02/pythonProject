from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice')

driver.find_element_by_css_selector("[class*=btn]").click()

print (driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)