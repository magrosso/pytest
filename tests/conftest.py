import pytest


# this is run once per module
@pytest.fixture(autouse=True, scope="module")
def setup_teardown_module():
    # code to be executed before the first test in the module
    # print("setup module".upper())
    yield
    # code to be executed after the last test in the module
    # print("teardown module".upper())


@pytest.fixture(autouse=True, scope="function")
def setup_tear_down_test_case():
    # code the be executed before each test
    # print("setup test case".upper())
    # a failed assertion inside a test setup or teardown fixture cause a test to ERROR instead of FAILED
    assert True
    yield
    # code to be executed after each test
    # print("teardown test case".upper())
