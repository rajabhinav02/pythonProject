import pytest


@pytest.mark.usefixtures("crossbrowser")
class Testmultilpe():

    def test_multipledata(self, crossbrowser):
        print (crossbrowser[0])
