"""Trivial greeting helper, unrelated to profile_utils.py.

Added deliberately to test that pushing an unrelated commit does not cause
the bot to falsely mark open findings in profile_utils.py as resolved.
"""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hi there, {name}!"
