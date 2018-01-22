import connexion
from swagger_server.models.client import Client
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def client_list(offset=None, limit=None, client_ids=None):
    """
    client_list
    
    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param client_ids: An optional list of client ids
    :type client_ids: List[int]

    :rtype: List[Client]
    """
    return 'do some magic!'


def client_read(client_id):
    """
    client_read
    
    :param client_id: A UUID value identifying the client
    :type client_id: str

    :rtype: Client
    """
    return 'do some magic!'


def user_delete(user_id):
    """
    user_delete
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def user_list(offset=None, limit=None, email=None, user_ids=None):
    """
    user_list
    
    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param email: An optional email filter
    :type email: str
    :param user_ids: An optional list of user ids
    :type user_ids: List[str]

    :rtype: List[User]
    """
    return 'do some magic!'


def user_read(user_id):
    """
    user_read
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def user_update(user_id, data=None):
    """
    user_update
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = User.from_dict(connexion.request.get_json())
    return 'do some magic!'
