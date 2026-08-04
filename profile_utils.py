"""Small user-profile helpers for the test-my-pr-review-bot demo repo."""


def get_display_name(user_data):
    """Return a display name built from the user's profile data."""
    return f"{user_data['first_name']} {user_data['last_name']}"


def get_role_label(user_data):
    """Return a human-readable label for the user's role."""
    role = user_data['role']
    return role.replace("_", " ").title()
