import pytest


def test_another(setup):
    a= "testing"
    print("second run")
    assert a == "testing", "what is this"

@pytest.mark.smoke
def test_calc():
    b=2
    c=4
    assert b+2==c, "calc wrong"

def test_creditcarddebit():
    print("credit card second")

@pytest.fixture()
def setup():
    print("execute first")
    yield
    print("exceute last")