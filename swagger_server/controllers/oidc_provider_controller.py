import connexion
import six

from swagger_server.models.client import Client  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def client_list(offset=None, limit=None, client_ids=None):  # noqa: E501
    """client_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param client_ids: An optional list of client ids
    :type client_ids: List[int]

    :rtype: List[Client]
    """
    return 'do some magic!'


def client_read(client_id):  # noqa: E501
    """client_read

     # noqa: E501

    :param client_id: A UUID value identifying the client
    :type client_id: dict | bytes

    :rtype: Client
    """
    if connexion.request.is_json:
        client_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_delete(user_id):  # noqa: E501
    """user_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_list(offset=None, limit=None, email=None, user_ids=None):  # noqa: E501
    """user_list

     # noqa: E501

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


def user_read(user_id):  # noqa: E501
    """user_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_update(user_id, data=None):  # noqa: E501
    """user_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
