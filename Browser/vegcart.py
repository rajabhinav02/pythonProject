from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

List=[]
List2=[]
driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

#driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_xpath("//*[@type='search']").send_keys("br")

count= len(driver.find_elements_by_css_selector("[class='product']"))
assert count==2

#button = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
#assert count==2

button = driver.find_elements_by_xpath("//div[@class='product']/div[3]/button")
#button = driver.find_elements_by_css_selector("div[class='product'] div button") #--css selector

print(len(button))

for co in button:
    names=co.find_element_by_xpath("parent::div/parent::div/h4").text
    List.append(names)
    co.click()

print(List)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
waiting= WebDriverWait(driver,10)
#waiting.until(expected_conditions.presence_of_element_located(By.XPATH))
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

#names2=driver.find_elements_by_css_selector("td p.product-name")
names2 = driver.find_elements_by_xpath("//p[@class='product-name']")
#//td/p[@class='product-name']


for nameagain in names2:
    names2=nameagain.text
    print(names2)
    #List2.append(names2)


#print (List2)

#assert List== List2

waiting.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='promoCode']")))
driver.find_element_by_xpath("//*[@class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element_by_xpath("//*[@class='promoBtn']").click()
waiting.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"[class='promoInfo']")))
print(driver.find_element_by_css_selector("[class='promoInfo']").text)

totalamount = driver.find_element_by_class_name("totAmt").text
waiting.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='discountAmt']")))
discamount = driver.find_element_by_xpath("//span[@class='discountAmt']").text

assert int(totalamount) > float(discamount)

amountforitems = driver.find_elements_by_xpath("//tr/td[5]/p")

sum=0
for peramount in amountforitems:
    peramountvalue= peramount.text
    sum= sum+int(peramountvalue)

assert int(sum)== int(totalamount)


#//tr/td[text()='30 ']
#//table[@id='product']//td[text()='Python Programming Language ']/following-sibling::td





