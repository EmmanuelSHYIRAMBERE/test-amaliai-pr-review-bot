"""Small user-profile helpers for the test-my-pr-review-bot demo repo."""


def get_display_name(user_data):
    """Return a display name built from the user's profile data."""
    first_name = user_data.get('first_name', '')
    last_name = user_data.get('last_name', '')
    return f"{first_name} {last_name}".strip()
