import connexion
from swagger_server.models.admin_note import AdminNote
from swagger_server.models.admin_note_update import AdminNoteUpdate
from swagger_server.models.country import Country
from swagger_server.models.country_update import CountryUpdate
from swagger_server.models.site_data_schema import SiteDataSchema
from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate
from swagger_server.models.user_site_data import UserSiteData
from swagger_server.models.user_site_data_update import UserSiteDataUpdate
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def adminnote_create(data=None):
    """
    adminnote_create
    
    :param data: 
    :type data: dict | bytes

    :rtype: AdminNote
    """
    if connexion.request.is_json:
        data = AdminNote.from_dict(connexion.request.get_json())
    return 'do some magic!'


def adminnote_delete(user_id, creator_id, created_at):
    """
    adminnote_delete
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param creator_id: The creator_id
    :type creator_id: str
    :param created_at: The created_at value
    :type created_at: str

    :rtype: None
    """
    created_at = deserialize_datetime(created_at)
    return 'do some magic!'


def adminnote_list(offset=None, limit=None, user_id=None, creator_id=None):
    """
    adminnote_list
    
    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: str
    :param creator_id: An optional query parameter to filter by creator (a user_id)
    :type creator_id: str

    :rtype: List[AdminNote]
    """
    return 'do some magic!'


def adminnote_read(user_id, creator_id, created_at):
    """
    adminnote_read
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param creator_id: The creator_id
    :type creator_id: str
    :param created_at: The created_at value
    :type created_at: str

    :rtype: AdminNote
    """
    created_at = deserialize_datetime(created_at)
    return 'do some magic!'


def adminnote_update(user_id, creator_id, created_at, data=None):
    """
    adminnote_update
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param creator_id: The creator_id
    :type creator_id: str
    :param created_at: The created_at value
    :type created_at: str
    :param data: 
    :type data: dict | bytes

    :rtype: AdminNote
    """
    created_at = deserialize_datetime(created_at)
    if connexion.request.is_json:
        data = AdminNoteUpdate.from_dict(connexion.request.get_json())
    return 'do some magic!'


def country_create(data=None):
    """
    country_create
    
    :param data: 
    :type data: dict | bytes

    :rtype: Country
    """
    if connexion.request.is_json:
        data = Country.from_dict(connexion.request.get_json())
    return 'do some magic!'


def country_delete(country_code):
    """
    country_delete
    
    :param country_code: A unique two-character value identifying the country.
    :type country_code: str

    :rtype: None
    """
    return 'do some magic!'


def country_list(limit=None, offset=None, country_codes=None):
    """
    country_list
    
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param country_codes: An optional list of country codes
    :type country_codes: List[str]

    :rtype: List[Country]
    """
    return 'do some magic!'


def country_read(country_code):
    """
    country_read
    
    :param country_code: A unique two-character value identifying the country.
    :type country_code: str

    :rtype: Country
    """
    return 'do some magic!'


def country_update(country_code, data=None):
    """
    country_update
    
    :param country_code: A unique two-character value identifying the country.
    :type country_code: str
    :param data: 
    :type data: dict | bytes

    :rtype: Country
    """
    if connexion.request.is_json:
        data = CountryUpdate.from_dict(connexion.request.get_json())
    return 'do some magic!'


def sitedataschema_create(data=None):
    """
    sitedataschema_create
    
    :param data: 
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    if connexion.request.is_json:
        data = SiteDataSchema.from_dict(connexion.request.get_json())
    return 'do some magic!'


def sitedataschema_delete(site_id):
    """
    sitedataschema_delete
    
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def sitedataschema_list(offset=None, limit=None, site_ids=None):
    """
    sitedataschema_list
    
    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param site_ids: An optional list of site ids
    :type site_ids: List[int]

    :rtype: List[SiteDataSchema]
    """
    return 'do some magic!'


def sitedataschema_read(site_id):
    """
    sitedataschema_read
    
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: SiteDataSchema
    """
    return 'do some magic!'


def sitedataschema_update(site_id, data=None):
    """
    sitedataschema_update
    
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data: 
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    if connexion.request.is_json:
        data = SiteDataSchemaUpdate.from_dict(connexion.request.get_json())
    return 'do some magic!'


def usersitedata_create(data=None):
    """
    usersitedata_create
    
    :param data: 
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        data = UserSiteData.from_dict(connexion.request.get_json())
    return 'do some magic!'


def usersitedata_delete(user_id, site_id):
    """
    usersitedata_delete
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def usersitedata_list(offset=None, limit=None, user_id=None, site_id=None):
    """
    usersitedata_list
    
    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: str
    :param site_id: An optional query parameter to filter by site_id
    :type site_id: int

    :rtype: List[UserSiteData]
    """
    return 'do some magic!'


def usersitedata_read(user_id, site_id):
    """
    usersitedata_read
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: UserSiteData
    """
    return 'do some magic!'


def usersitedata_update(user_id, site_id, data=None):
    """
    usersitedata_update
    
    :param user_id: A UUID value identifying the user.
    :type user_id: str
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data: 
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        data = UserSiteDataUpdate.from_dict(connexion.request.get_json())
    return 'do some magic!'
