#!/usr/bin/env python3
'''the auth module'''

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash the input password using bcrypt with a salt.
    Args:
        password (str): The input password to be hashed.
    Returns:
        bytes: The salted hash of the input password.
    """
    # Generate a random salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
