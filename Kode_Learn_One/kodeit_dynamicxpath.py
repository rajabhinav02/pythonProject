from selenium import webdriver
from selenium.webdriver.common.by import By


class dynamic:

    def xpathd(self):
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        baseurl = 'https://letskodeit.teachable.com/courses'
        driver.get(baseurl)

        textbox = driver.find_element(By.XPATH, "//input[@name='query']")
        textbox.send_keys("Java")

        coursename = "//div[contains( @class , 'course-listing-title') and contains (text(), '{0}')]"


        fullcoursename=coursename.format("JavaScript for")

        driver.find_element_by_xpath(fullcoursename).click()
        driver.switch_to.frame()
        driver.switch_to.default_content()

ab = dynamic()
#//div[contains(@class, 'course-listing-title') and contains (@text(), 'JavaScript for beginners')]
#//div[contains(@class, 'course-listing-title') and contains (text(), 'JavaScript for')]
ab.xpathd()
#
# FEI-- List of issues for FEI
# who is owning this up. which team is working.




