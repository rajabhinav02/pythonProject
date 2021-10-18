import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Kode_Learn_One.wrapperc import wrapping


class TestCase:

    def test_now(self):

        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

        baseurl = "https://rahulshettyacademy.com/angularpractice/"

        wp = wrapping(driver)


        driver.get(baseurl)

        #driver.find_element(By.XPATH, "//input[@name='name']").send_keys("first")
        wp.getElement("//input[@name='name']", "xpath").send_keys("first")
        driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("second")
        driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("third")

        time.sleep(10)

    def test_presence(self):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

        baseurl = "https://rahulshettyacademy.com/angularpractice/"

        wp = wrapping(driver)

        wp.getElementPresent("[name='email']", "css_selector")



hj = TestCase()
hj.test_now()
hj.test_presence()