"""Small inventory helpers for the test-my-pr-review-bot demo repo."""


def get_item_price(item_data):
    """Return the price of an item from its data dict."""
    return item_data.get('price')
