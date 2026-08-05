"""Small stats helpers for the test-my-pr-review-bot demo repo."""


def calculate_average(numbers: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    total = sum(numbers)
    return total / len(numbers)


def calculate_max_deviation(numbers: list[float]) -> float:
    """Return the largest absolute deviation from the average."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    avg = calculate_average(numbers)
    return max(abs(n - avg) for n in numbers)
