"""Small stats helpers for the test-my-pr-review-bot demo repo."""


def calculate_average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("cannot compute the average of an empty list")
    total = sum(numbers)
    return total / len(numbers)


def calculate_max_deviation(numbers):
    """Return the largest absolute deviation from the average."""
    avg = calculate_average(numbers)
    return max(abs(n - avg) for n in numbers)
