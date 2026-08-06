"""Small inventory helpers for the test-my-pr-review-bot demo repo.

See test_inventory.py for coverage of the missing-key and non-numeric cases.
"""


def get_item_price(item_data: dict) -> float:
    """Return the price of an item from its data dict.

    Raises ValueError if 'price' is missing or not numeric, matching the
    original fail-fast contract instead of silently returning None.
    """
    if 'price' not in item_data:
        raise ValueError("item_data must contain 'price'")
    price = item_data['price']
    if not isinstance(price, (int, float)):
        raise ValueError("item_data['price'] must be numeric")
    return float(price)
