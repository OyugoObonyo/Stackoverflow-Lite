"""

The abstract_user_query module: Contains abtsract class for querying users

This module contains definition of an abstract class useful in querying the
database's user table and also the subsequent implementation of the
abstract class
"""

from abc import ABC, abstractmethod


class AbtsractUserQueryModel(ABC):
    """

    AbstractUserQueryModel is to be adopted by any QueryUserModel object

    QueryUserModel objects are tasked with querying the User table in the
    database to retrieve object(s) that match a particular request
    """

    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_by_name(self, name):
        pass
