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

    password_byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_byte, salt)
    return hashed
