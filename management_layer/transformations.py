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

SITE_DATA_SCHEMA = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["site_id", "schema"]
)

USER_DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "domain_id", "role_id"]
)

USER_SITE_DATA = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string),
        Mapping("consented_at", conversion=datetime_to_string)
    ],
    copy_fields=["user_id", "site_id", "data", "blocked"]
)

