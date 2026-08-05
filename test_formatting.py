from formatting import shout


def test_shout_returns_uppercase_with_exclamation():
    assert shout("hello") == "HELLO!"


def test_shout_handles_empty_string():
    assert shout("") == "!"
