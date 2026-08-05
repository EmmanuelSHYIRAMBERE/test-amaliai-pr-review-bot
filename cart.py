"""Small shopping-cart helpers for the test-my-pr-review-bot demo repo."""

from typing import List, Optional, TypeVar

T = TypeVar("T")


def _fresh_list(value: Optional[List[T]]) -> List[T]:
    """Return value if given, otherwise a brand-new empty list.

    Centralizes the "mutable default argument" fix: callers pass None as the
    default and get a fresh list per call instead of one shared across calls.
    """
    return value if value is not None else []


def add_item(item: T, items: Optional[List[T]] = None) -> List[T]:
    """Add an item to the cart and return the updated cart."""
    items = _fresh_list(items)
    items.append(item)
    return items


def summarize_cart(cart_name: str, item: Optional[T] = None, cart: Optional[List[T]] = None) -> str:
    """Add an item (if given) to the named cart's running list and summarize it."""
    cart = _fresh_list(cart)
    if item is not None:
        cart.append(item)
    return f"{cart_name}: {len(cart)} item(s) -> {cart}"
