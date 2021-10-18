from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class wrapping:

    def __init__(self, driver):
        self.driver = driver

    def getBy(self,  locatortype):
        locatortype = locatortype.lower()

        if locatortype == "id":
            return By.ID
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css_selector":
            return By.CSS_SELECTOR
        elif locatortype == "link_text":
            return By.LINK_TEXT
        elif locatortype == "class_name":
            return By.CLASS_NAME

        else:
            print ("nothing")
            return False

    def getElement(self, locator, locatortype ="id"):

        element = None
        try:
            locatortype = locatortype.lower()
            byType= self.getBy(locatortype)
            element = self.driver.find_element(byType, locator)
            print("element found")

        except:
            print("element not found")

        return element

    def getElementPresent(self, locator, locatortype = "id"):

        locatortype = locatortype.lower()
        byType = self.getBy(locatortype)

        element = self.driver.find_elements(byType, locator)

        if len(element) > 0:
            print("element found")
            return True
        else:
            print("element not found")
            return False


    def waiting(self, locator, time, locatortype="id"):
        locatortype = locatortype.lower()
        byType = self.getBy(locatortype)

        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located(byType, locator))
