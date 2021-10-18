from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\ChromeDriver92\\chromedriver_win32 (5)\\chromedriver.exe")
driver.get("https://www.spicejet.com/")

slect = Select(driver.find_element_by_id("ctl00_mainContent_ddl_originStation1"))
slect.select_by_index(5)