"""Small inventory helpers for the test-my-pr-review-bot demo repo."""


def get_item_price(item_data: dict) -> float:
    """Return the price of an item from its data dict."""
    if 'price' not in item_data:
        raise ValueError("item_data must contain 'price'")
    return item_data['price']
