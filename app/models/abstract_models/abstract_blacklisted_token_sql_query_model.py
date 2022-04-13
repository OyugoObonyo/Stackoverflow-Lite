"""

The abstract_blacklisted_token_sql_query module: Contains abstract class for
querying the blacklisted_token table

This module contains definition of an abstract class useful in querying the
database's user table and also the subsequent implementation of the
abstract class
"""

from abc import ABC, abstractmethod


class AbstractBlacklistedTokenQueryModel(ABC):
    """

    AbstractBlacklistedTokenQueryModel is to be adopted by any QueryUserModel
    object

    AbstractBlacklistedTokenQueryModel objects are tasked with querying the
    blacklisted_tokens table in the db to retrieve object(s)
    that match a particular request
    """

    @abstractmethod
    def save(self):
        pass
