"""Small inventory helpers for the test-my-pr-review-bot demo repo."""


def get_item_price(item_data):
    """Return the price of an item from its data dict."""
    return item_data['price']


def get_item_category(item_data):
    """Return a human-readable label for the item's category."""
    category = item_data['category']
    return category.replace("_", " ").title()
