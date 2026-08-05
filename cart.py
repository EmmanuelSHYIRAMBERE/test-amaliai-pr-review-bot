"""Small shopping-cart helpers for the test-my-pr-review-bot demo repo."""


def add_item(item, items=[]):
    """Add an item to the cart and return the updated cart."""
    items.append(item)
    return items


def summarize_cart(cart_name, item=None, cart=[]):
    """Add an item (if given) to the named cart's running list and summarize it."""
    if item is not None:
        cart.append(item)
    return f"{cart_name}: {len(cart)} item(s) -> {cart}"
