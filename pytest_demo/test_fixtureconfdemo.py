import pytest

from pytest_demo.log_demo import logdemotest


@pytest.mark.usefixtures("dataload")
class Testuserprofile(logdemotest):

    def test_dataLoadcheck(self,dataload):
        #log=self.test_log()
        log=self.log()
        log.info(dataload[0])
        print(dataload[0])



