from typing import NamedTuple

# import pytest_check as check
from src.math import math
import pytest
import sys
import time


xfail = pytest.mark.xfail


# skip the whole test suite for
# Python versions less than 3.12 or
# Non Windows OS

pytestmark = [
    pytest.mark.skipif(
        condition=not sys.platform.startswith("win"),
        reason="Windows-only tests",
    ),
    pytest.mark.skipif(
        condition=sys.version_info < (3, 12), reason="Requires python 3.12"
    ),
]


@pytest.mark.parametrize("x, y, result", [(1, 2, 3), (-1, 0, -1), (123, -1, 122)])
def test_addition(x, y, result) -> None:
    assert math.add(x, y) == result
    assert math.add(y, x) == result


@pytest.mark.parametrize("x, y, result", [(1, 2, -1), (-1, 0, -1)])
def test_subtraction(x, y, result) -> None:
    assert math.sub(x, y) == result
    assert math.sub(-x, -y) == -result


@pytest.mark.parametrize(
    "x, y, result",
    [(1, 2, 2), pytest.param(-1, 0, 0, id="multiply by zero"), (-1, 6, -6)],
)
def test_multiplication(x, y, result) -> None:
    assert math.mul(x, y) == result
    # time.sleep(0.9)
    assert math.mul(y, x) == result


division_test_data = [(1, 2, 0), (10, 2, 5), (11, 2, 5), (3, 1, 3), (1002, 2, 501)]


@pytest.mark.parametrize("x, y, result", division_test_data)
def test_division(x, y, result) -> None:
    assert math.div(x, y) == result


@pytest.mark.parametrize(
    "x, y",
    [(1, 0), (10, 0), (-11, 0), pytest.param(3, 0, id="divide by zero")],
)
def test_division_fail(x, y) -> None:
    with pytest.raises(ValueError) as exc_info:
        assert math.div(x, y)
    (msg,) = exc_info.value.args
    assert msg.startswith("Cannot divide by zero")


class Input(NamedTuple):
    input: int

    expected: int


@pytest.mark.parametrize(
    "x, expected",
    (
        Input(input=0, expected=0),
        Input(input=1, expected=1),
        Input(input=10, expected=100),
        Input(input=11, expected=121),
        pytest.param(3, 10, marks=pytest.mark.xfail(condition="3*3==9")),
        pytest.param(12, 144, id="12*12==144"),
    ),
)
def test_square(x, expected) -> None:
    assert math.square(x) == expected
    assert math.square(-x) == expected


# skips test execution - not recommended, better use xfail


@pytest.mark.skip(reason="broken test")
def test_skipped(): ...


@pytest.mark.skipif(
    condition=sys.platform == "win32", reason="Test only applicable to Linux platform"
)
def test_skipped_conditionally(): ...


# test expected to fail that failed - result indicated by small 'x' or XFAIL in verbose mode


@xfail
def test_expected_to_fail_failed():
    assert False


# test expected to fail that unexpectedly succeeded - result indicated by capital 'X' or XPASS in verbose mode
# by default this condition will not fail the overall test result


@xfail
def test_expected_to_fail_but_passing():
    assert True


@xfail(strict=True)
def test_expected_to_fail_but_passing_fail():
    assert True


@xfail(strict=True)
def test_expected_to_fail_but_passing_fail_condition():
    assert True


def test_check_multiple_assertions(check):
    for num in {40, 77, 11, 23, 709}:
        with check:
            assert num > 10
    assert False
