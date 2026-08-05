from cart import add_item, summarize_cart


def test_add_item_uses_fresh_list_by_default():
    first = add_item("apple")
    second = add_item("banana")

    assert first == ["apple"]
    assert second == ["banana"]
    assert first is not second


def test_add_item_appends_to_caller_provided_list():
    caller_list = ["existing"]
    result = add_item("new", caller_list)

    assert result == ["existing", "new"]
    assert result is caller_list


def test_summarize_cart_uses_fresh_cart_by_default():
    first = summarize_cart("cart-a", "apple")
    second = summarize_cart("cart-b", "banana")

    assert first == "cart-a: 1 item(s) -> ['apple']"
    assert second == "cart-b: 1 item(s) -> ['banana']"


def test_summarize_cart_without_item_reports_existing_cart():
    result = summarize_cart("cart-c", cart=["x", "y"])
    assert result == "cart-c: 2 item(s) -> ['x', 'y']"
