"""Trivial formatting helper, unrelated to inventory.py.

Added deliberately to test that pushing an unrelated commit does not cause
the bot to falsely mark open findings in inventory.py as resolved.
"""


def shout(text: str) -> str:
    return text.upper() + "!"
