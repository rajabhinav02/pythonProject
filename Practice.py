import inspect
import logging
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumDrivers:
    def __init__(self,driver):
        self.driver= driver

    def GetByType(self,locatortype):

        locatortype= locatortype.lower()
        if locatortype == "id":
            return By.ID

    def getElement(self, locator, locatortype="id"):
        locatortype= locatortype.lower()
        getBytype= self.GetByType(locator, locatortype)
        element = self.driver.find_element(getBytype, locator)
        return element

   # def scrollUp(self, direction):
      #  if direction == "up"
           # self.driver.execute_script("window.scroll(0,-1000);")


    def viewscroll(self, locator, locatortype):
        locatortype= locatortype.lower()
        element= self.getElement(locator, locatortype)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switchframe(self, locator, locatortype):
        locatortype = locatortype.lower()
        self.driver.switch_to.frame(self.getElement(locator,locatortype))

    def waiting(self, time, locator, locatortype):
        byType = self.GetByType(locatortype)
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located((byType,locator)))

    def dropdown(self, value, locator, locatortype):
        element = self.getElement(locator, locatortype)
        select = Select(element)
        select.select_by_visible_text(value)

    def screenshot(self, resultmessage):
        screenshotfilename= resultmessage + str(time.time()*1000)+ ".png"
        screenshotdirectory = "../Screenshots/"
        relativefn = screenshotdirectory+screenshotfilename
        currentdirectory = os.path.dirname(__file__)
        destinationfilename = os.path.join(currentdirectory,relativefn)
        destinatindir = os.path.join(currentdirectory,screenshotdirectory)

        try:
            if not os.path.exists(destinatindir):
                os.makedirs(destinatindir)

            self.driver.save_screenshot(destinationfilename)

        except:
            print("haha")


    def logge(self, loglevel):
        tcname= inspect.stack()[1][3]
        logger= logging.getLogger(tcname)
        logger.setLevel(logging.DEBUG)
        fileHandler = logging.FileHandler("{0}.log".format(tcname), mode="a")
        fileHandler.setLevel(loglevel)
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(format)
        logger.addHandler(fileHandler)
        return logger




