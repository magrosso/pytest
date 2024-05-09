import pytest


@pytest.fixture(autouse=True, scope="module")
def setup_teardown():
    print("setup module")
    yield
    print("teardown module")


@pytest.fixture(autouse=True, scope="function")
def setup_tear_down_test_case():
    print("setup test case")
    yield
    print("teardown test case")
