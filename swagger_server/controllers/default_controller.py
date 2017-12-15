import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def sites_site_id_activate_get(site_id):
    """
    sites_site_id_activate_get
    Activate the site so that users can log in to it.
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def sites_site_id_deactivate_get(site_id):
    """
    sites_site_id_deactivate_get
    Deactivate the site so that users cannot log in to it.
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def users_user_id_activate_get(user_id):
    """
    users_user_id_activate_get
    Activate the user&#39;s account.
    :param user_id: A UUID value identifying the user.
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def users_user_id_deactivate_get(user_id):
    """
    users_user_id_deactivate_get
    Deactivate the user&#39;s account.
    :param user_id: A UUID value identifying the user.
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'
