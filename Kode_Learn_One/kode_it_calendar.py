from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(30)
baseurl = 'https://www.globalsqa.com/demo-site/datepicker/'
driver.get(baseurl)

driver.switch_to.frame(driver.find_element_by_xpath("//*[@class='demo-frame lazyloaded']"))

#driver.find_element_by_xpath()

datefield = "//input[@id='datepicker']"

driver.find_element_by_xpath(datefield).click()

calendar= driver.find_element_by_xpath("//table[@class='ui-datepicker-calendar']")

#"//table[@class='ui-datepicker-calendar']"

#driver.find_elements_by_tag_name()

dates=calendar.find_elements_by_xpath("//a")

for da in dates:

    if da.text == '7':
        da.click()
