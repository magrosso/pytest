from Typing import Generator


# return list
def generate_even_numbers(start: int, stop: int) -> list[int]:
    return [num for num in range(start, stop, 1) if num % 2 == 0]


def generate_odd_numbers(start: int, stop: int) -> Generator[int]:
    for num in range(start, stop):
        if num % 2 != 0:
            yield num
