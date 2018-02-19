from datetime import datetime, date

from management_layer.transformation import Transformation, Mapping


def datetime_to_string(x: datetime) -> str:
    return x.strftime("%Y:%m:%dT%H:%M:%SZ")


def datetime_to_string(x: date) -> str:
    return x.strftime("%Y:%m:%d")


ADMIN_NOTE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "user_id", "creator_id", "note"]
)

DOMAIN = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "parent_id", "name", "description"]
)

DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["domain_id", "role_id", "grant_implicitly"]
)

INVITATION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("expires_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "first_name", "last_name", "email",
                 "invitor_id", "is_system_user"]
)

INVITATION_DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["invitation_id", "domain_id", "role_id"]
)

INVITATION_SITE_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["invitation_id", "site_id", "role_id"]
)

PERMISSION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "name", "description"]
)

RESOURCE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "urn", "description"]
)

ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "label", "description", "requires_2fa"]
)

ROLE_RESOURCE_PERMISSION = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["role_id", "resource_id", "permission_id"]
)

SITE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["id", "name", "domain_id", "description",
                 "client_id", "is_active"]
)

SITE_DATA_SCHEMA = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["site_id", "schema"]
)

SITE_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["site_id", "role_id", "grant_implicitly"]
)

USER_DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "domain_id", "role_id"]
)

USER_SITE_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "site_id", "role_id"]
)

USER_SITE_DATA = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("consented_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "site_id", "data", "blocked"]
)

