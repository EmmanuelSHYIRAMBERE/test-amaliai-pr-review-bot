import pytest

from inventory import get_item_price


def test_get_item_price_returns_price():
    assert get_item_price({"price": 9.99}) == 9.99


def test_get_item_price_missing_key_raises():
    with pytest.raises(ValueError):
        get_item_price({})
