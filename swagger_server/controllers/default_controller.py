import connexion
import six

from swagger_server import util


def sites_site_id_activate_get(site_id):  # noqa: E501
    """sites_site_id_activate_get

    Activate the site so that users can log in to it. # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def sites_site_id_deactivate_get(site_id):  # noqa: E501
    """sites_site_id_deactivate_get

    Deactivate the site so that users cannot log in to it. # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def users_user_id_activate_get(user_id):  # noqa: E501
    """users_user_id_activate_get

    Activate the user&#39;s account. # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_deactivate_get(user_id):  # noqa: E501
    """users_user_id_deactivate_get

    Deactivate the user&#39;s account. # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
