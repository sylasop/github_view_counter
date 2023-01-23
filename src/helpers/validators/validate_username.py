import re


def validate_username(username: str) -> bool:
    """
    Validate the username passed in the request.
    """
    if username is None:
        return False
    if not re.match("^[a-zA-Z0-9_]{1,38}$", username):
        return False
    return True
