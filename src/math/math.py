import logging

logger = logging.getLogger(name=__name__)
logger.level = logging.DEBUG  # log all levels!


def add(x: int, y: int) -> int:
    logger.info(f"add({x}, {y})")
    return x + y


def sub(x: int, y: int) -> int:
    logger.info(f"sub({x}, {y})")
    return x - y


def mul(x: int, y: int) -> int:
    logger.info(f"mul({x}, {y})")
    return x * y


def div(x: int, y: int) -> int:
    logger.info(f"div({x}, {y})")
    return x // y


def square(x: int) -> int:
    logger.info(f"add({x}^2")
    return x**2
