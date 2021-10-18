import pytest



@pytest.mark.smoke
@pytest.mark.xfail
def test_first():
    print("first demo")

@pytest.mark.skip
def test_creditcardpay():
    print("credit card one")