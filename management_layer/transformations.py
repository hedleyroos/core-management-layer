from datetime import datetime

from management_layer.transformation import Transformation, Mapping


def datetime_to_string(x: datetime) -> str:
    return x.strftime("%Y:%m:%dT%H:%M:%SZ")


DOMAIN_ROLE = Transformation(
    mappings=[
        Mapping("created_at", conversion=datetime_to_string),
        Mapping("updated_at", conversion=datetime_to_string)
    ],
    copy_fields=["domain_id", "role_id", "grant_implicitly"]
)


