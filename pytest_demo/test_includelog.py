import pytest
from selenium import webdriver

from pytest_demo.log_demo import logdemotest

@pytest.mark.usefixtures("newtest")
class Testmultiplelog(logdemotest):
    driver = None
    def test_logmultiple(self,newtest):
        log=self.log()
        log.info(newtest[1])
        print (newtest)

    @pytest.fixture()
    def test(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # return driver
        #print("Fixture")

    #@pytest.mark.usefixtures("test")
    def test_method(self, test):
        #driver=Testmultiplelog.test()
        driver.get("https://www.google.com")
        print(driver.title)
