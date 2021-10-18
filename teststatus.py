from Practice import SeleniumDrivers


class TestStatus(SeleniumDrivers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.testlist= []

    def TestStatus(self,result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.testlist.append("Pass")
                else:
                    self.testlist.append("Fail")
            else:
                self.testlist.append("Fail")

        except:
            self.testlist.append("Fail")

    def mark(self, result, resultmessage):
        self.TestStatus(result,resultmessage)

    def markfinal(self, tcname, result, resultmessage):
        self.TestStatus(result, resultmessage)

        if "Fail" in self.testlist:
            self.testlist.clear()
            assert True==False

        else:
            self.testlist.clear()
            assert True==True



