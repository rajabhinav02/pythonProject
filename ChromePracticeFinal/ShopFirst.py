from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("headless")
#chrome_options.add_argument("--ignore-certificate-errors")

driver=webdriver.Chrome(executable_path='C:\\chromedriver_win32\\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/angularpractice/shop')

waiting=WebDriverWait(driver,5)
waiting.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@class='btn btn-info']")))

AddButtons=driver.find_elements_by_xpath("//button[@class='btn btn-info']")

for Add in AddButtons:
    Brand=Add.find_element_by_xpath("parent:: div/ parent::div/div[1]/h4/a").text
    if Brand== "Blackberry":
        Add.click()

driver.find_element_by_xpath("//a[contains(@class, 'btn')]").click()

waiting.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[@class='btn btn-danger']")))

assert driver.find_element_by_xpath("//h4[@class='media-heading']/a").text== Brand,"wrong selection"

driver.find_element_by_xpath("//*[@class='btn btn-success']").click()

driver.find_element_by_xpath("//input[contains(@class, 'validate')]").send_keys("Ind")
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div/div[2]/ul/li/a ")))
countries=driver.find_elements_by_xpath("//div/div[2]/ul/li/a")

for country in countries:
    if country.text=="India":
        country.click()
        break

selected=driver.find_element_by_css_selector("[class*='validate']").get_attribute('value')

assert selected== "India","wrong country selected"

tnc= driver.find_element_by_xpath("//label[@for='checkbox2']")
tnc.click()
try:
    assert tnc.is_selected()

except:
    driver.find_element_by_xpath("//input[@type='submit']").click()

    msg=driver.find_element_by_css_selector("[class*='alert-success']").text
    print("in except")
    print(msg)
    assert "Success" in msg

driver.get_screenshot_as_file("screen.png")

