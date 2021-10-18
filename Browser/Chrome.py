from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.com")

driver.maximize_window()
print(driver.title)