import pytest

from stats import calculate_average, calculate_max_deviation


def test_calculate_average_normal_input():
    assert calculate_average([1, 2, 3]) == 2


def test_calculate_average_empty_raises():
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_max_deviation_normal_input():
    assert calculate_max_deviation([1, 2, 3]) == 1


def test_calculate_max_deviation_empty_raises():
    with pytest.raises(ValueError):
        calculate_max_deviation([])
