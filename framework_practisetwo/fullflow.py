import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

baseurl = "https://rahulshettyacademy.com/angularpractice/"

driver.get(baseurl)

name = "Abhi"
email = "Raj"
password="haha"


namelocation = driver.find_element(By.XPATH,"//input[@name='name']")
emailloaction = driver.find_element(By.CSS_SELECTOR,"[name='email']")
passwordlocation = driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1")
icecheckboxlocation = driver.find_element(By.ID,"exampleCheck1")
genderlocation = driver.find_element(By.ID, "exampleFormControlSelect1")
empstatus = driver.find_elements(By.XPATH, "//input[@type='radio']")
datelocation = driver.find_element(By.CSS_SELECTOR, "[name='bday']")
submitlocation = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
shoplocation =driver.find_element(By.LINK_TEXT, "Shop")




namelocation.send_keys(name)
emailloaction.send_keys(email)
passwordlocation.send_keys(password)
icecheckboxlocation.click()
gender = Select(genderlocation)
gender.select_by_index(1)

for radio in empstatus:
    radio.click()
    time.sleep(3)

assert not empstatus[2].is_enabled()

datelocation.click()
datelocation.send_keys("12")
datelocation.send_keys("06")
datelocation.send_keys("2012")
submitlocation.click()

successlocation = driver.find_element(By.XPATH, "//div[contains (@class, 'alert-success')]")

assert "Success" in successlocation.text
time.sleep(3)

shoplocation.click()

addbuttonslocation = driver.find_elements(By.XPATH, "//button[contains(@class, 'btn-info')]")
checkoutlocation = driver.find_element(By.CSS_SELECTOR, "[class*='nav-link btn']")

for add in addbuttonslocation:
    brandname = add.find_element_by_xpath("parent::div/parent::div//h4").text
    if brandname == 'Blackberry':
        add.click()

checkoutlocation.click()

brandnameselected = driver.find_element(By.XPATH, "//h4[@class='media-heading']/a")
pricelocation = driver.find_element(By.XPATH, "//table[contains (@class, 'table')]//tr/td[3]/strong")
totalamountlocation = driver.find_element(By.XPATH, "//table[contains (@class, 'table')]//tr/td[4]/strong")
finalcheckoutlocation = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-success')]")

brandname2 =brandnameselected.text

assert brandname == brandname2

price = pricelocation.text
totalamount = totalamountlocation.text

print(price)
print(totalamount)

finalcheckoutlocation.click()

countrylocation = driver.find_element(By.CSS_SELECTOR, "#country")
#displayedcountrylocation = driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")
#tnccheckboxlocation = driver.find_element(By.XPATH, "//input[@type='checkbox']")
#purchasebuttonlocation = driver.find_element(By.XPATH, "//input[contains (@class, 'btn-success') and (@type='submit')]")


countrylocation.send_keys("In")

wait = WebDriverWait(driver,30)

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))

displayedcountrylocation = driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")

for country in displayedcountrylocation:
    #cn = country.text

    if country.text == "India":
        country.click()
        break

purchasebuttonlocation = driver.find_element(By.XPATH, "//input[contains (@class, 'btn-success') and (@type='submit')]")
#tnccheckboxlocation.click()
purchasebuttonlocation.click()

successmsglocation = driver.find_element(By.XPATH, "//strong")
finalmsg = successmsglocation.text

assert "Success" in finalmsg



















