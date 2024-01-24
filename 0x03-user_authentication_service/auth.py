#!/usr/bin/env python3
'''the auth module'''

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


def _generate_uuid() -> str:
    """
    return a uuid string
    """
    return str(uuid.uuid4())


class Auth():
    '''the Auth class to interact with the authentication database'''

    def __init__(self):
        '''initializes the class'''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user.
        Args:
            email (str): User's email.
            password (str): User's password.
        Returns:
            User: The created User object.
        Raises:
            ValueError: If a user with the provided email already exists.
        """
        # Check if the user with the given email already exists
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        code = _hash_password(password).decode('utf-8')
        new_user = self._db.add_user(email, code)

        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(
                    password.encode(), user.hashed_password.encode()
            ):
                return True
            else:
                return False
        except NoResultFound:
            return False
