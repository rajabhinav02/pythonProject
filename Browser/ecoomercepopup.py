import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("http://automationpractice.com/index.php?id_category=3&controller=category")
time.sleep(5)
elm= driver.find_element_by_xpath("//a[contains(@class, 'ui-slider-handle')][1]")
driver.execute_script("arguments[0].scrollIntoView(true);",elm)
element = driver.find_element(By.CSS_SELECTOR, ".available-now")

driver.execute_script("arguments[0].scrollIntoView(true);", element)
action = ActionChains(driver)
time.sleep(4)

action.drag_and_drop_by_offset(elm, 500,0)

elements= driver.find_elements(By.CSS_SELECTOR, ".available-now")
for element in elements:
    action.move_to_element(element).perform()
    print("moved")

    break

driver.find_element_by_xpath("//span[text()='Add to cart']").click()
print("clicked")
#print(driver.current_window_handle)
#driver.switch_to.window(driver.window_handles[1])
#al=driver.switch_to.alert
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Proceed')]"))).click()
#driver.find_element_by_xpath("//span[contains(text(), 'Proceed')]").click()
#al.accept()

