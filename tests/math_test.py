from src.math import math
import pytest


@pytest.mark.parametrize("x, y, result", [(1, 2, 3), (-1, 0, -1)])
def test_addition(x, y, result) -> None:
    print(f"testing add({x},{y})")
    assert math.add(x, y) == result


# @pytest.mark.usefixtures("setup_teardown")
@pytest.mark.parametrize("x, y, result", [(1, 2, -1), (-1, 0, -1)])
def test_subtraction(x, y, result) -> None:
    print(f"testing sub({x},{y})")
    assert math.sub(x, y) == result


@pytest.mark.parametrize("x, y, result", [(1, 2, 2), (-1, 0, 0), (-1, 6, -6)])
def test_multiplication(x, y, result) -> None:
    print(f"testing mul({x},{y})")
    assert math.mul(x, y) == result


@pytest.mark.parametrize("x, y, result", [(1, 2, 0), (10, 2, 5), (11, 2, 5), (3, 1, 3)])
def test_division(x, y, result) -> None:
    print(f"testing div({x},{y})")
    assert math.div(x, y) == result


@pytest.mark.parametrize("x, y", [(1, 0), (10, 0), (-11, 0), (3, 0)])
def test_division_fail(x, y) -> None:
    print(f"testing div{x},{y}")
    with pytest.raises(ZeroDivisionError):
        assert math.div(x, y)


@pytest.mark.parametrize("x, result", [(1, 1), (10, 100), (11, 121), (3, 9)])
def test_square(x, result) -> None:
    print(f"testing square({x})")
    assert math.square(x)
