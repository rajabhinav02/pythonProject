from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Kode_Learn_One.wrapperc import wrapping


class waite:

    def __init__(self, driver):
        self.driver=driver
        self.wp = wrapping()

    def waiting(self, locator, time, locatortype="id"):
        locatortype= locatortype.lower()
        byType= self.wp.getBy(locatortype)

        wait = WebDriverWait(self.driver, time)
        element=wait.until(EC.element_to_be_clickable((byType, locator)))
        return element