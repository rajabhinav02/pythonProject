from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

parent_window= driver.current_window_handle
print(parent_window)
driver.find_element_by_link_text("Click Here").click()
childs = driver.window_handles

print(type(childs))
for child in childs:
    print(child)
    if parent_window!= child:
        driver.switch_to.window(child)
        print(driver.find_element_by_xpath("//h3").text)
        driver.close()
driver.switch_to.window(parent_window)



# driver.switch_to.window(driver.window_handles[1])
# print(driver.find_element_by_xpath("//h3").text)
