import pytest


@pytest.mark.usefixtures("confsetup")
class TestFixtureDemo:


    def test_first(self):
        print("in between one")


    def test_second(self):
        print("in between two")
