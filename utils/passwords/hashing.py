"""

A module that contains a helper function
which generates a hash for a given password
"""

import bcrypt


def generate_password_hash(password: str):
    """

    generate_password_hash generates a hash from a given password
    :password: password to be hashed
    :return: a hash of the given password of type bytes
    """

    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password_byte, salt)
    return hash.decode("utf-8")


def check_password_hash(password: str, hash: bytes) -> bool:
    """

    check_password_hash checks whether a password matches a particular hash
    :password: password to be checked
    :hash: hash of given password
    :return: True if password matches and false if it doesn't
    """

    encoded_password = password.encode("utf-8")
    match = bcrypt.checkpw(encoded_password, hash.encode("utf-8"))
    return match
