"""Small user-profile helpers for the test-my-pr-review-bot demo repo."""


def get_display_name(user_data):
    """Return a display name built from the user's profile data."""
    return f"{user_data['first_name']} {user_data['last_name']}"
