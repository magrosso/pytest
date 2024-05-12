import logging

logger = logging.getLogger(name=__name__)
logger.level = logging.DEBUG  # log all levels!


class MathError(ValueError): ...


def add(x: int, y: int) -> int:
    logger.debug(f"({x=}, {y=})")
    return x + y


def sub(x: int, y: int) -> int:
    logger.debug(f"{x}, {y}")
    return x - y


def mul(x: int, y: int) -> int:
    logger.debug(f"({x}, {y})")
    return x * y


def div(x: int, y: int) -> int:
    logger.debug(f"({x}, {y})")
    if y == 0:
        raise MathError("Cannot divide by zero!")
    return x // y


def square(x: int) -> int:
    logger.debug(f"({x}^2)")
    return x**2


def increment(x: int) -> int:
    return x + 1


def decrement(x: int) -> int:
    return x - 1
