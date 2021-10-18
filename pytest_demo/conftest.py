import pytest

@pytest.fixture(scope="class")
def confsetup():
    print ("Testing the fixture first")
    yield
    print ("Testing the fixture second")

@pytest.fixture()
def dataload():
    print("testing the data parameter")
    return ["Abhi", "New", "Test"]


@pytest.fixture(params=[("chrome","test", "yes"), ("firefox","haha"), "ie"])
def crossbrowser(request):
    return request.param


@pytest.fixture(params=[("Test1", "Test4", "Test7"), ("Test2",""), ("Test3", "Test6")])
def newtest(request):
    return request.param

