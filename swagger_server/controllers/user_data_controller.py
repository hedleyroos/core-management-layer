import connexion
import six

from swagger_server.models.admin_note import AdminNote  # noqa: E501
from swagger_server.models.admin_note_create import AdminNoteCreate  # noqa: E501
from swagger_server.models.admin_note_update import AdminNoteUpdate  # noqa: E501
from swagger_server.models.site_data_schema import SiteDataSchema  # noqa: E501
from swagger_server.models.site_data_schema_create import SiteDataSchemaCreate  # noqa: E501
from swagger_server.models.site_data_schema_update import SiteDataSchemaUpdate  # noqa: E501
from swagger_server.models.user_site_data import UserSiteData  # noqa: E501
from swagger_server.models.user_site_data_create import UserSiteDataCreate  # noqa: E501
from swagger_server.models.user_site_data_update import UserSiteDataUpdate  # noqa: E501
from swagger_server import util


def adminnote_create(data=None):  # noqa: E501
    """adminnote_create

     # noqa: E501

    :param data: 
    :type data: dict | bytes

    :rtype: AdminNote
    """
    if connexion.request.is_json:
        data = AdminNoteCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def adminnote_delete(user_id, creator_id, created_at):  # noqa: E501
    """adminnote_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param creator_id: The creator_id
    :type creator_id: dict | bytes
    :param created_at: The created_at value
    :type created_at: str

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        creator_id = .from_dict(connexion.request.get_json())  # noqa: E501
    created_at = util.deserialize_datetime(created_at)
    return 'do some magic!'


def adminnote_list(offset=None, limit=None, user_id=None, creator_id=None):  # noqa: E501
    """adminnote_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: dict | bytes
    :param creator_id: An optional query parameter to filter by creator (a user_id)
    :type creator_id: dict | bytes

    :rtype: List[AdminNote]
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        creator_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def adminnote_read(user_id, creator_id, created_at):  # noqa: E501
    """adminnote_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param creator_id: The creator_id
    :type creator_id: dict | bytes
    :param created_at: The created_at value
    :type created_at: str

    :rtype: AdminNote
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        creator_id = .from_dict(connexion.request.get_json())  # noqa: E501
    created_at = util.deserialize_datetime(created_at)
    return 'do some magic!'


def adminnote_update(user_id, creator_id, created_at, data=None):  # noqa: E501
    """adminnote_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param creator_id: The creator_id
    :type creator_id: dict | bytes
    :param created_at: The created_at value
    :type created_at: str
    :param data: 
    :type data: dict | bytes

    :rtype: AdminNote
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        creator_id = .from_dict(connexion.request.get_json())  # noqa: E501
    created_at = util.deserialize_datetime(created_at)
    if connexion.request.is_json:
        data = AdminNoteUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sitedataschema_create(data=None):  # noqa: E501
    """sitedataschema_create

     # noqa: E501

    :param data: 
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    if connexion.request.is_json:
        data = SiteDataSchemaCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sitedataschema_delete(site_id):  # noqa: E501
    """sitedataschema_delete

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    return 'do some magic!'


def sitedataschema_list(offset=None, limit=None, site_ids=None):  # noqa: E501
    """sitedataschema_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param site_ids: An optional list of site ids
    :type site_ids: List[int]

    :rtype: List[SiteDataSchema]
    """
    return 'do some magic!'


def sitedataschema_read(site_id):  # noqa: E501
    """sitedataschema_read

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: SiteDataSchema
    """
    return 'do some magic!'


def sitedataschema_update(site_id, data=None):  # noqa: E501
    """sitedataschema_update

     # noqa: E501

    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data: 
    :type data: dict | bytes

    :rtype: SiteDataSchema
    """
    if connexion.request.is_json:
        data = SiteDataSchemaUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_create(data=None):  # noqa: E501
    """usersitedata_create

     # noqa: E501

    :param data: 
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        data = UserSiteDataCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_delete(user_id, site_id):  # noqa: E501
    """usersitedata_delete

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_list(offset=None, limit=None, user_id=None, site_id=None):  # noqa: E501
    """usersitedata_list

     # noqa: E501

    :param offset: An optional query parameter specifying the offset in the result set to start from.
    :type offset: int
    :param limit: An optional query parameter to limit the number of results returned.
    :type limit: int
    :param user_id: An optional query parameter to filter by user_id
    :type user_id: dict | bytes
    :param site_id: An optional query parameter to filter by site_id
    :type site_id: int

    :rtype: List[UserSiteData]
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_read(user_id, site_id):  # noqa: E501
    """usersitedata_read

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usersitedata_update(user_id, site_id, data=None):  # noqa: E501
    """usersitedata_update

     # noqa: E501

    :param user_id: A UUID value identifying the user.
    :type user_id: dict | bytes
    :param site_id: A unique integer value identifying the site.
    :type site_id: int
    :param data: 
    :type data: dict | bytes

    :rtype: UserSiteData
    """
    if connexion.request.is_json:
        user_id = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        data = UserSiteDataUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
