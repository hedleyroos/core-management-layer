"""
Do not modify this file. It is generated from the Swagger specification.

"""
import importlib
import logging
import json
import jsonschema
import os
from jsonschema import ValidationError
from aiohttp.web import View, json_response, Response, HTTPNoContent

import management_layer.api.schemas as schemas
import management_layer.api.utils as utils

# Set up logging
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

VALIDATE_RESPONSES = os.getenv("SWAGGER_API_VALIDATE_RESPONSES", False)
LOGGER.info("Swagger API response validation is {}".format(
    "on" if VALIDATE_RESPONSES else "off"
))

# Set up the stub class. If it is not explicitly configured in the settings.py
# file of the project, we default to a mocked class.
stub_class_path = os.getenv("STUBS_CLASS", "management_layer.api.stubs.MockedStubClass")
module_name, class_name = stub_class_path.rsplit(".", 1)
Module = importlib.import_module(module_name)
Stubs = getattr(Module, class_name)

TOTAL_COUNT_HEADER = "X-Total-Count"


def maybe_validate_result(result, schema):
    if VALIDATE_RESPONSES:
        try:
            jsonschema.validate(result, schema)
        except ValidationError as e:
            LOGGER.error(e.message)


class Adminnotes(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "creator_id": {
                "description": "The user making the request will be considered the creator and thus this field is not available when creating admin note.",
                "format": "uuid",
                "readOnly": true,
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "note": {
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "id",
            "user_id",
            "creator_id",
            "note",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.admin_note
    POST_BODY_SCHEMA = schemas.admin_note_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Adminnotes instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # user_id (optional): string An optional query parameter to filter by user_id
            value = self.request.query.get("user_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["user_id"] = value
            # creator_id (optional): string An optional query parameter to filter by creator (a user_id)
            value = self.request.query.get("creator_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["creator_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.adminnote_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Adminnotes instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.adminnote_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class AdminnotesAdminNoteId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.admin_note
    PUT_RESPONSE_SCHEMA = schemas.admin_note
    PUT_BODY_SCHEMA = schemas.admin_note_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A AdminnotesAdminNoteId instance
        """
        try:
            # admin_note_id: integer A unique integer value identifying the admin note.
            admin_note_id = self.request.match_info["admin_note_id"]
            admin_note_id = int(admin_note_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.adminnote_delete(
            self.request, admin_note_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A AdminnotesAdminNoteId instance
        """
        try:
            # admin_note_id: integer A unique integer value identifying the admin note.
            admin_note_id = self.request.match_info["admin_note_id"]
            admin_note_id = int(admin_note_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.adminnote_read(
            self.request, admin_note_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A AdminnotesAdminNoteId instance
        """
        try:
            # admin_note_id: integer A unique integer value identifying the admin note.
            admin_note_id = self.request.match_info["admin_note_id"]
            admin_note_id = int(admin_note_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.adminnote_update(
            self.request, body, admin_note_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Clients(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "_post_logout_redirect_uris": {
                "description": "New-line delimited list of post-logout redirect URIs",
                "type": "string"
            },
            "_redirect_uris": {
                "description": "New-line delimited list of redirect URIs",
                "type": "string"
            },
            "client_id": {
                "description": "",
                "type": "string"
            },
            "contact_email": {
                "description": "",
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "logo": {
                "description": "",
                "format": "uri",
                "type": "string"
            },
            "name": {
                "description": "",
                "type": "string"
            },
            "require_consent": {
                "description": "If disabled, the Server will NEVER ask the user for consent.",
                "type": "boolean"
            },
            "response_type": {
                "description": "",
                "type": "string"
            },
            "reuse_consent": {
                "description": "If enabled, the Server will save the user consent given to a specific client, so that user will not be prompted for the same authorization multiple times.",
                "type": "boolean"
            },
            "terms_url": {
                "description": "External reference to the privacy policy of the client.",
                "type": "string"
            },
            "website_url": {
                "description": "",
                "type": "string"
            }
        },
        "required": [
            "id",
            "client_id",
            "response_type"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Clients instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # client_ids (optional): array An optional list of client ids
            value = self.request.query.get("client_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["client_ids"] = value
            # client_id (optional): string An optional client id to filter on. This is not the primary key.
            value = self.request.query.get("client_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["client_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.client_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})


class ClientsClientId(View):

    GET_RESPONSE_SCHEMA = schemas.client

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A ClientsClientId instance
        """
        try:
            # client_id: string A string value identifying the client
            client_id = self.request.match_info["client_id"]
            jsonschema.validate(client_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.client_read(
            self.request, client_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Domainroles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "grant_implicitly": {
                "type": "boolean"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "domain_id",
            "role_id",
            "grant_implicitly",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.domain_role
    POST_BODY_SCHEMA = schemas.domain_role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Domainroles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # domain_id (optional): integer An optional query parameter to filter by domain_id
            value = self.request.query.get("domain_id", None)
            if value is not None:
                value = int(value)
                optional_args["domain_id"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domainrole_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Domainroles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.domainrole_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class DomainrolesDomainIdRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.domain_role
    PUT_RESPONSE_SCHEMA = schemas.domain_role
    PUT_BODY_SCHEMA = schemas.domain_role_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A DomainrolesDomainIdRoleId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domainrole_delete(
            self.request, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A DomainrolesDomainIdRoleId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domainrole_read(
            self.request, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A DomainrolesDomainIdRoleId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.domainrole_update(
            self.request, body, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Domains(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "name": {
                "maxLength": 100,
                "type": "string"
            },
            "parent_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "name",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.domain
    POST_BODY_SCHEMA = schemas.domain_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Domains instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # domain_ids (optional): array An optional list of domain ids
            value = self.request.query.get("domain_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["domain_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domain_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Domains instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.domain_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class DomainsDomainId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.domain
    PUT_RESPONSE_SCHEMA = schemas.domain
    PUT_BODY_SCHEMA = schemas.domain_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A DomainsDomainId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domain_delete(
            self.request, domain_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A DomainsDomainId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domain_read(
            self.request, domain_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A DomainsDomainId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.domain_update(
            self.request, body, domain_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Invitationdomainroles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "invitation_id": {
                "format": "uuid",
                "type": "string"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "invitation_id",
            "domain_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.invitation_domain_role
    POST_BODY_SCHEMA = schemas.invitation_domain_role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Invitationdomainroles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # invitation_id (optional): string An optional query parameter to filter by invitation_id
            value = self.request.query.get("invitation_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["invitation_id"] = value
            # domain_id (optional): integer An optional query parameter to filter by domain_id
            value = self.request.query.get("domain_id", None)
            if value is not None:
                value = int(value)
                optional_args["domain_id"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationdomainrole_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Invitationdomainroles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.invitationdomainrole_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class InvitationdomainrolesInvitationIdDomainIdRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.invitation_domain_role

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationdomainrolesInvitationIdDomainIdRoleId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationdomainrole_delete(
            self.request, invitation_id, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationdomainrolesInvitationIdDomainIdRoleId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationdomainrole_read(
            self.request, invitation_id, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Invitations(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "email": {
                "format": "email",
                "type": "string"
            },
            "expires_at": {
                "format": "date-time",
                "type": "string"
            },
            "first_name": {
                "maxLength": 100,
                "type": "string"
            },
            "id": {
                "format": "uuid",
                "readOnly": true,
                "type": "string"
            },
            "invitor_id": {
                "description": "The user that created the invitation",
                "format": "uuid",
                "type": "string"
            },
            "last_name": {
                "maxLength": 100,
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "invitor_id",
            "first_name",
            "last_name",
            "email",
            "expires_at",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.invitation
    POST_BODY_SCHEMA = schemas.invitation_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Invitations instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # invitor_id (optional): string Optional filter based on the invitor (the user who created the invitation)
            value = self.request.query.get("invitor_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["invitor_id"] = value
            # invitation_ids (optional): array An optional list of invitation ids
            value = self.request.query.get("invitation_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["invitation_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitation_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Invitations instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.invitation_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class InvitationsInvitationId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.invitation
    PUT_RESPONSE_SCHEMA = schemas.invitation
    PUT_BODY_SCHEMA = schemas.invitation_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationsInvitationId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitation_delete(
            self.request, invitation_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationsInvitationId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitation_read(
            self.request, invitation_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationsInvitationId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.invitation_update(
            self.request, body, invitation_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Invitationsiteroles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "invitation_id": {
                "format": "uuid",
                "type": "string"
            },
            "role_id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "invitation_id",
            "site_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.invitation_site_role
    POST_BODY_SCHEMA = schemas.invitation_site_role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Invitationsiteroles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # invitation_id (optional): string An optional query parameter to filter by invitation_id
            value = self.request.query.get("invitation_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["invitation_id"] = value
            # site_id (optional): integer An optional query parameter to filter by site_id
            value = self.request.query.get("site_id", None)
            if value is not None:
                value = int(value)
                optional_args["site_id"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationsiterole_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Invitationsiteroles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.invitationsiterole_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class InvitationsiterolesInvitationIdSiteIdRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.invitation_site_role

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationsiterolesInvitationIdSiteIdRoleId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationsiterole_delete(
            self.request, invitation_id, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A InvitationsiterolesInvitationIdSiteIdRoleId instance
        """
        try:
            # invitation_id: string A UUID value identifying the invitation.
            invitation_id = self.request.match_info["invitation_id"]
            jsonschema.validate(invitation_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationsiterole_read(
            self.request, invitation_id, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class OpsAllUserRolesUserId(View):

    GET_RESPONSE_SCHEMA = schemas.all_user_roles

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsAllUserRolesUserId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_all_user_roles(
            self.request, user_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class OpsDomainRolesDomainId(View):

    GET_RESPONSE_SCHEMA = schemas.domain_roles

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsDomainRolesDomainId instance
        """
        try:
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_domain_roles(
            self.request, domain_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class OpsSiteAndDomainRolesSiteId(View):

    GET_RESPONSE_SCHEMA = schemas.site_and_domain_roles

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsSiteAndDomainRolesSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_site_and_domain_roles(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class OpsSiteRoleLabelsAggregatedSiteId(View):

    GET_RESPONSE_SCHEMA = schemas.site_role_labels_aggregated

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsSiteRoleLabelsAggregatedSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_site_role_labels_aggregated(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class OpsUserSiteRoleLabelsAggregatedUserIdSiteId(View):

    GET_RESPONSE_SCHEMA = schemas.user_site_role_labels_aggregated

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsUserSiteRoleLabelsAggregatedUserIdSiteId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_user_site_role_labels_aggregated(
            self.request, user_id, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Permissions(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "name": {
                "maxLength": 50,
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "name",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.permission
    POST_BODY_SCHEMA = schemas.permission_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Permissions instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # permission_ids (optional): array An optional list of permission ids
            value = self.request.query.get("permission_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["permission_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.permission_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Permissions instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.permission_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class PermissionsPermissionId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.permission
    PUT_RESPONSE_SCHEMA = schemas.permission
    PUT_BODY_SCHEMA = schemas.permission_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PermissionsPermissionId instance
        """
        try:
            # permission_id: integer A unique integer value identifying the permission.
            permission_id = self.request.match_info["permission_id"]
            permission_id = int(permission_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.permission_delete(
            self.request, permission_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PermissionsPermissionId instance
        """
        try:
            # permission_id: integer A unique integer value identifying the permission.
            permission_id = self.request.match_info["permission_id"]
            permission_id = int(permission_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.permission_read(
            self.request, permission_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A PermissionsPermissionId instance
        """
        try:
            # permission_id: integer A unique integer value identifying the permission.
            permission_id = self.request.match_info["permission_id"]
            permission_id = int(permission_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.permission_update(
            self.request, body, permission_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Resources(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "urn": {
                "format": "uri",
                "type": "string"
            }
        },
        "required": [
            "id",
            "urn",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.resource
    POST_BODY_SCHEMA = schemas.resource_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Resources instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # prefix (optional): string An optional URN prefix filter
            value = self.request.query.get("prefix", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["prefix"] = value
            # resource_ids (optional): array An optional list of resource ids
            value = self.request.query.get("resource_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["resource_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.resource_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Resources instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.resource_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class ResourcesResourceId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.resource
    PUT_RESPONSE_SCHEMA = schemas.resource
    PUT_BODY_SCHEMA = schemas.resource_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A ResourcesResourceId instance
        """
        try:
            # resource_id: integer A unique integer value identifying the resource.
            resource_id = self.request.match_info["resource_id"]
            resource_id = int(resource_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.resource_delete(
            self.request, resource_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A ResourcesResourceId instance
        """
        try:
            # resource_id: integer A unique integer value identifying the resource.
            resource_id = self.request.match_info["resource_id"]
            resource_id = int(resource_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.resource_read(
            self.request, resource_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A ResourcesResourceId instance
        """
        try:
            # resource_id: integer A unique integer value identifying the resource.
            resource_id = self.request.match_info["resource_id"]
            resource_id = int(resource_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.resource_update(
            self.request, body, resource_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Roleresourcepermissions(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "permission_id": {
                "type": "integer"
            },
            "resource_id": {
                "type": "integer"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "role_id",
            "resource_id",
            "permission_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.role_resource_permission
    POST_BODY_SCHEMA = schemas.role_resource_permission_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Roleresourcepermissions instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
            # resource_id (optional): integer An optional resource filter
            value = self.request.query.get("resource_id", None)
            if value is not None:
                value = int(value)
                optional_args["resource_id"] = value
            # permission_id (optional): integer An optional permission filter
            value = self.request.query.get("permission_id", None)
            if value is not None:
                value = int(value)
                optional_args["permission_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.roleresourcepermission_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Roleresourcepermissions instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.roleresourcepermission_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class RoleresourcepermissionsRoleIdResourceIdPermissionId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.role_resource_permission

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RoleresourcepermissionsRoleIdResourceIdPermissionId instance
        """
        try:
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            # resource_id: integer A unique integer value identifying the resource.
            resource_id = self.request.match_info["resource_id"]
            resource_id = int(resource_id)
            # permission_id: integer A unique integer value identifying the permission.
            permission_id = self.request.match_info["permission_id"]
            permission_id = int(permission_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.roleresourcepermission_delete(
            self.request, role_id, resource_id, permission_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RoleresourcepermissionsRoleIdResourceIdPermissionId instance
        """
        try:
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            # resource_id: integer A unique integer value identifying the resource.
            resource_id = self.request.match_info["resource_id"]
            resource_id = int(resource_id)
            # permission_id: integer A unique integer value identifying the permission.
            permission_id = self.request.match_info["permission_id"]
            permission_id = int(permission_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.roleresourcepermission_read(
            self.request, role_id, resource_id, permission_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Roles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "label": {
                "maxLength": 100,
                "type": "string",
                "x-scope": [
                    "",
                    "#/definitions/role"
                ]
            },
            "requires_2fa": {
                "type": "boolean"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "label",
            "requires_2fa",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.role
    POST_BODY_SCHEMA = schemas.role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Roles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # role_ids (optional): array An optional list of role ids
            value = self.request.query.get("role_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["role_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.role_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Roles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.role_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class RolesRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.role
    PUT_RESPONSE_SCHEMA = schemas.role
    PUT_BODY_SCHEMA = schemas.role_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RolesRoleId instance
        """
        try:
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.role_delete(
            self.request, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RolesRoleId instance
        """
        try:
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.role_read(
            self.request, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RolesRoleId instance
        """
        try:
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.role_update(
            self.request, body, role_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Sitedataschemas(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "schema": {
                "type": "object"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "site_id",
            "schema",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.site_data_schema
    POST_BODY_SCHEMA = schemas.site_data_schema_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Sitedataschemas instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # site_ids (optional): array An optional list of site ids
            value = self.request.query.get("site_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["site_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.sitedataschema_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Sitedataschemas instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.sitedataschema_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class SitedataschemasSiteId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.site_data_schema
    PUT_RESPONSE_SCHEMA = schemas.site_data_schema
    PUT_BODY_SCHEMA = schemas.site_data_schema_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitedataschemasSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.sitedataschema_delete(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitedataschemasSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.sitedataschema_read(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitedataschemasSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.sitedataschema_update(
            self.request, body, site_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Siteroles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "grant_implicitly": {
                "type": "boolean"
            },
            "role_id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "site_id",
            "role_id",
            "grant_implicitly",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.site_role
    POST_BODY_SCHEMA = schemas.site_role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Siteroles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # site_id (optional): integer An optional query parameter to filter by site_id
            value = self.request.query.get("site_id", None)
            if value is not None:
                value = int(value)
                optional_args["site_id"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.siterole_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Siteroles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.siterole_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class SiterolesSiteIdRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.site_role
    PUT_RESPONSE_SCHEMA = schemas.site_role
    PUT_BODY_SCHEMA = schemas.site_role_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SiterolesSiteIdRoleId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.siterole_delete(
            self.request, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SiterolesSiteIdRoleId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.siterole_read(
            self.request, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SiterolesSiteIdRoleId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.siterole_update(
            self.request, body, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Sites(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "client_id": {
                "format": "uuid",
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "id": {
                "readOnly": true,
                "type": "integer"
            },
            "is_active": {
                "type": "boolean"
            },
            "name": {
                "maxLength": 100,
                "type": "string"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "domain_id",
            "name",
            "is_active",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.site
    POST_BODY_SCHEMA = schemas.site_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Sites instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # site_ids (optional): array An optional list of site ids
            value = self.request.query.get("site_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["site_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.site_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Sites instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.site_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class SitesSiteId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.site
    PUT_RESPONSE_SCHEMA = schemas.site
    PUT_BODY_SCHEMA = schemas.site_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitesSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.site_delete(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitesSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.site_read(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitesSiteId instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.site_update(
            self.request, body, site_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class SitesSiteIdActivate(View):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitesSiteIdActivate instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get__api_v1_sites_site_id_activate(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class SitesSiteIdDeactivate(View):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A SitesSiteIdDeactivate instance
        """
        try:
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get__api_v1_sites_site_id_deactivate(
            self.request, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Userdomainroles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer"
            },
            "role_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "user_id",
            "domain_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.user_domain_role
    POST_BODY_SCHEMA = schemas.user_domain_role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Userdomainroles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # user_id (optional): string An optional query parameter to filter by user_id
            value = self.request.query.get("user_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["user_id"] = value
            # domain_id (optional): integer An optional query parameter to filter by domain_id
            value = self.request.query.get("domain_id", None)
            if value is not None:
                value = int(value)
                optional_args["domain_id"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.userdomainrole_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Userdomainroles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.userdomainrole_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class UserdomainrolesUserIdDomainIdRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.user_domain_role

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserdomainrolesUserIdDomainIdRoleId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.userdomainrole_delete(
            self.request, user_id, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UserdomainrolesUserIdDomainIdRoleId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.userdomainrole_read(
            self.request, user_id, domain_id, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Users(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "avatar": {
                "format": "uri",
                "type": "string"
            },
            "birth_date": {
                "format": "date",
                "type": "string"
            },
            "country_code": {
                "maxLength": 2,
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "date_joined": {
                "description": "",
                "format": "date",
                "readOnly": true,
                "type": "string"
            },
            "email": {
                "description": "",
                "format": "email",
                "type": "string"
            },
            "email_verified": {
                "type": "boolean"
            },
            "first_name": {
                "description": "",
                "type": "string"
            },
            "gender": {
                "type": "string"
            },
            "id": {
                "description": "The UUID of the user",
                "format": "uuid",
                "readOnly": true,
                "type": "string"
            },
            "is_active": {
                "description": "Designates whether this user should be treated as active. Deselect this instead of deleting accounts.",
                "type": "boolean"
            },
            "last_login": {
                "description": "",
                "readOnly": true,
                "type": "string"
            },
            "last_name": {
                "description": "",
                "type": "string"
            },
            "msisdn": {
                "maxLength": 15,
                "type": "string"
            },
            "msisdn_verified": {
                "type": "boolean"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "username": {
                "description": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                "readOnly": true,
                "type": "string"
            }
        },
        "required": [
            "id",
            "username",
            "is_active",
            "date_joined",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Users instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # email (optional): string An optional email filter
            value = self.request.query.get("email", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["email"] = value
            # username_prefix (optional): string An optional username prefix filter
            value = self.request.query.get("username_prefix", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["username_prefix"] = value
            # user_ids (optional): array An optional list of user ids
            value = self.request.query.get("user_ids", None)
            if value is not None:
                jsonschema.validate(value, {"type": "array"})
                optional_args["user_ids"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.user_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})


class UsersUserId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.user
    PUT_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    PUT_BODY_SCHEMA = schemas.user

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersUserId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.user_delete(
            self.request, user_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersUserId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.user_read(
            self.request, user_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersUserId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.user_update(
            self.request, body, user_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class UsersUserIdActivate(View):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersUserIdActivate instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get__api_v1_users_user_id_activate(
            self.request, user_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class UsersUserIdDeactivate(View):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersUserIdDeactivate instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get__api_v1_users_user_id_deactivate(
            self.request, user_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class Usersitedata(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "blocked": {
                "type": "boolean"
            },
            "consented_at": {
                "format": "date",
                "type": "string"
            },
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "data": {
                "type": "object"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "user_id",
            "site_id",
            "consented_at",
            "blocked",
            "data",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.user_site_data
    POST_BODY_SCHEMA = schemas.user_site_data_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Usersitedata instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # user_id (optional): string An optional query parameter to filter by user_id
            value = self.request.query.get("user_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["user_id"] = value
            # site_id (optional): integer An optional query parameter to filter by site_id
            value = self.request.query.get("site_id", None)
            if value is not None:
                value = int(value)
                optional_args["site_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersitedata_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Usersitedata instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.usersitedata_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class UsersitedataUserIdSiteId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.user_site_data
    PUT_RESPONSE_SCHEMA = schemas.user_site_data
    PUT_BODY_SCHEMA = schemas.user_site_data_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersitedataUserIdSiteId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersitedata_delete(
            self.request, user_id, site_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersitedataUserIdSiteId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersitedata_read(
            self.request, user_id, site_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersitedataUserIdSiteId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.PUT_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.usersitedata_update(
            self.request, body, user_id, site_id, **optional_args)
        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result)


class Usersiteroles(View):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "role_id": {
                "type": "integer"
            },
            "site_id": {
                "type": "integer"
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string"
            }
        },
        "required": [
            "user_id",
            "site_id",
            "role_id",
            "created_at",
            "updated_at"
        ],
        "type": "object",
        "x-scope": [
            ""
        ]
    },
    "type": "array"
}""")
    POST_RESPONSE_SCHEMA = schemas.user_site_role
    POST_BODY_SCHEMA = schemas.user_site_role_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Usersiteroles instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            value = self.request.query.get("offset", None)
            if value is not None:
                value = int(value)
                optional_args["offset"] = value
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            value = self.request.query.get("limit", None)
            if value is not None:
                value = int(value)
                optional_args["limit"] = value
            # user_id (optional): string An optional query parameter to filter by user_id
            value = self.request.query.get("user_id", None)
            if value is not None:
                jsonschema.validate(value, {"type": "string"})
                optional_args["user_id"] = value
            # site_id (optional): integer An optional query parameter to filter by site_id
            value = self.request.query.get("site_id", None)
            if value is not None:
                value = int(value)
                optional_args["site_id"] = value
            # role_id (optional): integer An optional query parameter to filter by role_id
            value = self.request.query.get("role_id", None)
            if value is not None:
                value = int(value)
                optional_args["role_id"] = value
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersiterole_list(
            self.request, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers={TOTAL_COUNT_HEADER: "100"})

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Usersiteroles instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        try:
            body = await self.request.json()
            if not body:
                return Response(status=400, text="Body required")

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.usersiterole_create(
            self.request, body, **optional_args)
        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201)


class UsersiterolesUserIdSiteIdRoleId(View):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.user_site_role

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersiterolesUserIdSiteIdRoleId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersiterole_delete(
            self.request, user_id, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A UsersiterolesUserIdSiteIdRoleId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            # role_id: integer A unique integer value identifying the role.
            role_id = self.request.match_info["role_id"]
            role_id = int(role_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersiterole_read(
            self.request, user_id, site_id, role_id, **optional_args)
        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result)


class __SWAGGER_SPEC__(View):
    SPEC = json.loads("""{
    "basePath": "/api/v1",
    "definitions": {
        "admin_note": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "creator_id": {
                    "description": "The user making the request will be considered the creator and thus this field is not available when creating admin note.",
                    "format": "uuid",
                    "readOnly": true,
                    "type": "string"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "note": {
                    "type": "string"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "id",
                "user_id",
                "creator_id",
                "note",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "admin_note_create": {
            "properties": {
                "creator_id": {
                    "description": "The user making the request will be considered the creator and thus this field is not available when creating admin note.",
                    "format": "uuid",
                    "readOnly": true,
                    "type": "string"
                },
                "note": {
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "creator_id",
                "note"
            ],
            "type": "object"
        },
        "admin_note_update": {
            "minProperties": 1,
            "properties": {
                "note": {
                    "type": "string"
                }
            },
            "type": "object"
        },
        "all_user_roles": {
            "description": "An object containing the effective roles that a user has in any place in the organisational tree.",
            "properties": {
                "roles_map": {
                    "additionalProperties": {
                        "items": {
                            "type": "integer"
                        },
                        "type": "array"
                    },
                    "description": "Domain and site roles",
                    "example": {
                        "d:1": [
                            1
                        ],
                        "d:2": [
                            1,
                            2
                        ],
                        "s:1": [
                            1,
                            2,
                            3
                        ]
                    },
                    "type": "object"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "roles_map"
            ],
            "type": "object"
        },
        "client": {
            "properties": {
                "_post_logout_redirect_uris": {
                    "description": "New-line delimited list of post-logout redirect URIs",
                    "type": "string"
                },
                "_redirect_uris": {
                    "description": "New-line delimited list of redirect URIs",
                    "type": "string"
                },
                "client_id": {
                    "description": "",
                    "type": "string"
                },
                "contact_email": {
                    "description": "",
                    "type": "string"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "logo": {
                    "description": "",
                    "format": "uri",
                    "type": "string"
                },
                "name": {
                    "description": "",
                    "type": "string"
                },
                "require_consent": {
                    "description": "If disabled, the Server will NEVER ask the user for consent.",
                    "type": "boolean"
                },
                "response_type": {
                    "description": "",
                    "type": "string"
                },
                "reuse_consent": {
                    "description": "If enabled, the Server will save the user consent given to a specific client, so that user will not be prompted for the same authorization multiple times.",
                    "type": "boolean"
                },
                "terms_url": {
                    "description": "External reference to the privacy policy of the client.",
                    "type": "string"
                },
                "website_url": {
                    "description": "",
                    "type": "string"
                }
            },
            "required": [
                "id",
                "client_id",
                "response_type"
            ],
            "type": "object"
        },
        "domain": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "parent_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "id",
                "name",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "domain_create": {
            "properties": {
                "description": {
                    "type": "string"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "parent_id": {
                    "type": "integer"
                }
            },
            "required": [
                "name"
            ],
            "type": "object"
        },
        "domain_role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer"
                },
                "grant_implicitly": {
                    "type": "boolean"
                },
                "role_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "domain_id",
                "role_id",
                "grant_implicitly",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "domain_role_create": {
            "properties": {
                "domain_id": {
                    "type": "integer"
                },
                "grant_implicitly": {
                    "type": "boolean"
                },
                "role_id": {
                    "type": "integer"
                }
            },
            "required": [
                "domain_id",
                "role_id"
            ],
            "type": "object"
        },
        "domain_role_update": {
            "minProperties": 1,
            "properties": {
                "grant_implicitly": {
                    "type": "boolean"
                }
            },
            "type": "object"
        },
        "domain_roles": {
            "description": "An object containing the domain roles defined for a given domain and its lineage.",
            "properties": {
                "domain_id": {
                    "description": "The domain for which the request was made.",
                    "type": "integer"
                },
                "roles_map": {
                    "additionalProperties": {
                        "description": "The list of role ids for the domain",
                        "items": {
                            "type": "integer"
                        },
                        "type": "array"
                    },
                    "description": "A dictionary where the keys are domain ids prefixed with `d:` and the values are lists of role ids.",
                    "example": {
                        "d:1": [
                            1
                        ],
                        "d:2": [
                            1,
                            2
                        ],
                        "s:1": [
                            1,
                            2,
                            3
                        ]
                    },
                    "type": "object"
                }
            },
            "required": [
                "domain_id",
                "roles_map"
            ],
            "type": "object"
        },
        "domain_update": {
            "minProperties": 1,
            "properties": {
                "description": {
                    "type": "string"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "parent_id": {
                    "type": "integer"
                }
            },
            "type": "object"
        },
        "invitation": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "email": {
                    "format": "email",
                    "type": "string"
                },
                "expires_at": {
                    "format": "date-time",
                    "type": "string"
                },
                "first_name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "id": {
                    "format": "uuid",
                    "readOnly": true,
                    "type": "string"
                },
                "invitor_id": {
                    "description": "The user that created the invitation",
                    "format": "uuid",
                    "type": "string"
                },
                "last_name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "id",
                "invitor_id",
                "first_name",
                "last_name",
                "email",
                "expires_at",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "invitation_create": {
            "properties": {
                "email": {
                    "format": "email",
                    "type": "string"
                },
                "expires_at": {
                    "format": "date-time",
                    "type": "string"
                },
                "first_name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "invitor_id": {
                    "description": "The user that created the invitation",
                    "format": "uuid",
                    "type": "string"
                },
                "last_name": {
                    "maxLength": 100,
                    "type": "string"
                }
            },
            "required": [
                "invitor_id",
                "first_name",
                "last_name",
                "email"
            ],
            "type": "object"
        },
        "invitation_domain_role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer"
                },
                "invitation_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "role_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "invitation_id",
                "domain_id",
                "role_id",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "invitation_domain_role_create": {
            "properties": {
                "domain_id": {
                    "type": "integer"
                },
                "invitation_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "role_id": {
                    "type": "integer"
                }
            },
            "required": [
                "invitation_id",
                "domain_id",
                "role_id"
            ],
            "type": "object"
        },
        "invitation_site_role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "invitation_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "role_id": {
                    "type": "integer"
                },
                "site_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "invitation_id",
                "site_id",
                "role_id",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "invitation_site_role_create": {
            "properties": {
                "invitation_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "role_id": {
                    "type": "integer"
                },
                "site_id": {
                    "type": "integer"
                }
            },
            "required": [
                "invitation_id",
                "site_id",
                "role_id"
            ],
            "type": "object"
        },
        "invitation_update": {
            "minProperties": 1,
            "properties": {
                "email": {
                    "format": "email",
                    "type": "string"
                },
                "expires_at": {
                    "format": "date-time",
                    "type": "string"
                },
                "first_name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "last_name": {
                    "maxLength": 100,
                    "type": "string"
                }
            },
            "type": "object"
        },
        "permission": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "name": {
                    "maxLength": 50,
                    "type": "string"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "id",
                "name",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "permission_create": {
            "properties": {
                "description": {
                    "type": "string"
                },
                "name": {
                    "maxLength": 50,
                    "type": "string"
                }
            },
            "required": [
                "name"
            ],
            "type": "object"
        },
        "permission_update": {
            "minProperties": 1,
            "properties": {
                "description": {
                    "type": "string"
                },
                "name": {
                    "maxLength": 50,
                    "type": "string"
                }
            },
            "type": "object"
        },
        "resource": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "urn": {
                    "format": "uri",
                    "type": "string"
                }
            },
            "required": [
                "id",
                "urn",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "resource_create": {
            "properties": {
                "description": {
                    "type": "string"
                },
                "urn": {
                    "format": "uri",
                    "type": "string"
                }
            },
            "required": [
                "urn"
            ],
            "type": "object"
        },
        "resource_update": {
            "minProperties": 1,
            "properties": {
                "description": {
                    "type": "string"
                },
                "urn": {
                    "format": "uri",
                    "type": "string"
                }
            },
            "type": "object"
        },
        "role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "label": {
                    "maxLength": 100,
                    "type": "string",
                    "x-scope": [
                        "",
                        "#/definitions/role"
                    ]
                },
                "requires_2fa": {
                    "type": "boolean"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "id",
                "label",
                "requires_2fa",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "role_create": {
            "properties": {
                "description": {
                    "type": "string"
                },
                "label": {
                    "$ref": "#/definitions/role_label",
                    "x-scope": [
                        "",
                        "#/definitions/role_create"
                    ]
                },
                "requires_2fa": {
                    "type": "boolean"
                }
            },
            "required": [
                "label",
                "requires_2fa"
            ],
            "type": "object"
        },
        "role_label": {
            "maxLength": 100,
            "type": "string"
        },
        "role_resource_permission": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "permission_id": {
                    "type": "integer"
                },
                "resource_id": {
                    "type": "integer"
                },
                "role_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "role_id",
                "resource_id",
                "permission_id",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "role_resource_permission_create": {
            "properties": {
                "permission_id": {
                    "type": "integer"
                },
                "resource_id": {
                    "type": "integer"
                },
                "role_id": {
                    "type": "integer"
                }
            },
            "required": [
                "role_id",
                "resource_id",
                "permission_id"
            ],
            "type": "object"
        },
        "role_update": {
            "minProperties": 1,
            "properties": {
                "description": {
                    "type": "string"
                },
                "label": {
                    "maxLength": 100,
                    "type": "string"
                },
                "requires_2fa": {
                    "type": "boolean"
                }
            },
            "type": "object"
        },
        "site": {
            "properties": {
                "client_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer"
                },
                "id": {
                    "readOnly": true,
                    "type": "integer"
                },
                "is_active": {
                    "type": "boolean"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "id",
                "domain_id",
                "name",
                "is_active",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "site_and_domain_roles": {
            "description": "An object containing the site- and domain lineage roles defined for a given site.",
            "properties": {
                "roles_map": {
                    "additionalProperties": {
                        "description": "The list of role ids for the site or domain",
                        "items": {
                            "type": "integer"
                        },
                        "type": "array"
                    },
                    "description": "A dictionary where the keys are site and domain ids prefixed with `s:` and `d:`, respectively and the values are lists of role ids.",
                    "example": {
                        "d:1": [
                            1
                        ],
                        "d:2": [
                            1,
                            2
                        ],
                        "s:1": [
                            1,
                            2,
                            3
                        ]
                    }
                },
                "site_id": {
                    "description": "The site for which the request was made.",
                    "type": "integer"
                }
            },
            "required": [
                "site_id",
                "roles_map"
            ],
            "type": "object"
        },
        "site_create": {
            "properties": {
                "client_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer"
                },
                "is_active": {
                    "type": "boolean"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                }
            },
            "required": [
                "domain_id",
                "name"
            ],
            "type": "object"
        },
        "site_data_schema": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "schema": {
                    "type": "object"
                },
                "site_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "site_id",
                "schema",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "site_data_schema_create": {
            "properties": {
                "schema": {
                    "type": "object"
                },
                "site_id": {
                    "type": "integer"
                }
            },
            "required": [
                "site_id",
                "schema"
            ],
            "type": "object"
        },
        "site_data_schema_update": {
            "minProperties": 1,
            "properties": {
                "schema": {
                    "type": "object"
                }
            },
            "type": "object"
        },
        "site_role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "grant_implicitly": {
                    "type": "boolean"
                },
                "role_id": {
                    "type": "integer"
                },
                "site_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "site_id",
                "role_id",
                "grant_implicitly",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "site_role_create": {
            "properties": {
                "grant_implicitly": {
                    "type": "boolean"
                },
                "role_id": {
                    "type": "integer"
                },
                "site_id": {
                    "type": "integer"
                }
            },
            "required": [
                "site_id",
                "role_id"
            ],
            "type": "object"
        },
        "site_role_labels_aggregated": {
            "description": "An object containing a site ID and an aggregated list of all the role labels supported by the site and all the domains in its lineage.",
            "properties": {
                "roles": {
                    "items": {
                        "$ref": "#/definitions/role_label",
                        "x-scope": [
                            "",
                            "#/definitions/site_role_labels_aggregated"
                        ]
                    },
                    "type": "array"
                },
                "site_id": {
                    "type": "integer"
                }
            },
            "type": "object"
        },
        "site_role_update": {
            "minProperties": 1,
            "properties": {
                "grant_implicitly": {
                    "type": "boolean"
                }
            },
            "type": "object"
        },
        "site_update": {
            "minProperties": 1,
            "properties": {
                "client_id": {
                    "format": "uuid",
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer"
                },
                "is_active": {
                    "type": "boolean"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                }
            },
            "type": "object"
        },
        "user": {
            "properties": {
                "avatar": {
                    "format": "uri",
                    "type": "string"
                },
                "birth_date": {
                    "format": "date",
                    "type": "string"
                },
                "country_code": {
                    "maxLength": 2,
                    "type": "string"
                },
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "date_joined": {
                    "description": "",
                    "format": "date",
                    "readOnly": true,
                    "type": "string"
                },
                "email": {
                    "description": "",
                    "format": "email",
                    "type": "string"
                },
                "email_verified": {
                    "type": "boolean"
                },
                "first_name": {
                    "description": "",
                    "type": "string"
                },
                "gender": {
                    "type": "string"
                },
                "id": {
                    "description": "The UUID of the user",
                    "format": "uuid",
                    "readOnly": true,
                    "type": "string"
                },
                "is_active": {
                    "description": "Designates whether this user should be treated as active. Deselect this instead of deleting accounts.",
                    "type": "boolean"
                },
                "last_login": {
                    "description": "",
                    "readOnly": true,
                    "type": "string"
                },
                "last_name": {
                    "description": "",
                    "type": "string"
                },
                "msisdn": {
                    "maxLength": 15,
                    "type": "string"
                },
                "msisdn_verified": {
                    "type": "boolean"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "username": {
                    "description": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                    "readOnly": true,
                    "type": "string"
                }
            },
            "required": [
                "id",
                "username",
                "is_active",
                "date_joined",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "user_domain_role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer"
                },
                "role_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "domain_id",
                "role_id",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "user_domain_role_create": {
            "properties": {
                "domain_id": {
                    "type": "integer"
                },
                "role_id": {
                    "type": "integer"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "domain_id",
                "role_id"
            ],
            "type": "object"
        },
        "user_site_data": {
            "properties": {
                "blocked": {
                    "type": "boolean"
                },
                "consented_at": {
                    "format": "date",
                    "type": "string"
                },
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "data": {
                    "type": "object"
                },
                "site_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "site_id",
                "consented_at",
                "blocked",
                "data",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "user_site_data_create": {
            "properties": {
                "blocked": {
                    "type": "boolean"
                },
                "consented_at": {
                    "format": "date",
                    "type": "string"
                },
                "data": {
                    "type": "object"
                },
                "site_id": {
                    "type": "integer"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "site_id",
                "data"
            ],
            "type": "object"
        },
        "user_site_data_update": {
            "minProperties": 1,
            "properties": {
                "blocked": {
                    "type": "boolean"
                },
                "consented_at": {
                    "format": "date",
                    "type": "string"
                },
                "data": {
                    "type": "object"
                }
            },
            "type": "object"
        },
        "user_site_role": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "role_id": {
                    "type": "integer"
                },
                "site_id": {
                    "type": "integer"
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "site_id",
                "role_id",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "user_site_role_create": {
            "properties": {
                "role_id": {
                    "type": "integer"
                },
                "site_id": {
                    "type": "integer"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "required": [
                "user_id",
                "site_id",
                "role_id"
            ],
            "type": "object"
        },
        "user_site_role_labels_aggregated": {
            "description": "An object containing a user ID, site ID and an aggregated list of all the role labels assigned to the user for the site and all the domains in its lineage.",
            "properties": {
                "roles": {
                    "items": {
                        "$ref": "#/definitions/role_label",
                        "x-scope": [
                            "",
                            "#/definitions/user_site_role_labels_aggregated"
                        ]
                    },
                    "type": "array"
                },
                "site_id": {
                    "type": "integer"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string"
                }
            },
            "type": "object"
        },
        "user_update": {
            "minProperties": 1,
            "properties": {
                "avatar": {
                    "format": "uri",
                    "type": "string"
                },
                "birth_date": {
                    "format": "date",
                    "type": "string"
                },
                "country_code": {
                    "maxLength": 2,
                    "type": "string"
                },
                "email": {
                    "description": "",
                    "format": "email",
                    "type": "string"
                },
                "email_verified": {
                    "type": "boolean"
                },
                "first_name": {
                    "description": "",
                    "type": "string"
                },
                "gender": {
                    "type": "string"
                },
                "is_active": {
                    "description": "Designates whether this user should be treated as active. Deselect this instead of deleting accounts.",
                    "type": "boolean"
                },
                "last_name": {
                    "description": "",
                    "type": "string"
                },
                "msisdn": {
                    "maxLength": 15,
                    "type": "string"
                },
                "msisdn_verified": {
                    "type": "boolean"
                }
            },
            "type": "object"
        }
    },
    "host": "localhost:5000",
    "info": {
        "description": "The Management Layer API exposes the functionality that is available to users. Access to this API is based on a user token that must be presented with every request.\\n\\nThe Management Layer ties together the User Data Store, Access Control System and Authentication Service. It performs permission checking and audit logging.\\n",
        "title": "Management Layer API",
        "version": ""
    },
    "parameters": {
        "admin_note_id": {
            "description": "A unique integer value identifying the admin note.",
            "in": "path",
            "name": "admin_note_id",
            "required": true,
            "type": "integer"
        },
        "client_id": {
            "description": "A string value identifying the client",
            "format": "string",
            "in": "path",
            "name": "client_id",
            "required": true,
            "type": "string"
        },
        "country_code": {
            "description": "A unique two-character value identifying the country.",
            "in": "path",
            "maxLength": 2,
            "minLength": 2,
            "name": "country_code",
            "required": true,
            "type": "string"
        },
        "domain_id": {
            "description": "A unique integer value identifying the domain.",
            "in": "path",
            "name": "domain_id",
            "required": true,
            "type": "integer"
        },
        "invitation_id": {
            "description": "A UUID value identifying the invitation.",
            "format": "uuid",
            "in": "path",
            "name": "invitation_id",
            "required": true,
            "type": "string"
        },
        "optional_domain_filter": {
            "description": "An optional query parameter to filter by domain_id",
            "in": "query",
            "name": "domain_id",
            "required": false,
            "type": "integer"
        },
        "optional_invitation_filter": {
            "description": "An optional query parameter to filter by invitation_id",
            "format": "uuid",
            "in": "query",
            "name": "invitation_id",
            "required": false,
            "type": "string"
        },
        "optional_limit": {
            "default": 20,
            "description": "An optional query parameter to limit the number of results returned.",
            "in": "query",
            "maximum": 100,
            "minimum": 1,
            "name": "limit",
            "required": false,
            "type": "integer"
        },
        "optional_offset": {
            "default": 0,
            "description": "An optional query parameter specifying the offset in the result set to start from.",
            "in": "query",
            "minimum": 0,
            "name": "offset",
            "required": false,
            "type": "integer"
        },
        "optional_role_filter": {
            "description": "An optional query parameter to filter by role_id",
            "in": "query",
            "name": "role_id",
            "required": false,
            "type": "integer"
        },
        "optional_site_filter": {
            "description": "An optional query parameter to filter by site_id",
            "in": "query",
            "name": "site_id",
            "required": false,
            "type": "integer"
        },
        "optional_user_filter": {
            "description": "An optional query parameter to filter by user_id",
            "format": "uuid",
            "in": "query",
            "name": "user_id",
            "required": false,
            "type": "string"
        },
        "permission_id": {
            "description": "A unique integer value identifying the permission.",
            "in": "path",
            "name": "permission_id",
            "required": true,
            "type": "integer"
        },
        "resource_id": {
            "description": "A unique integer value identifying the resource.",
            "in": "path",
            "name": "resource_id",
            "required": true,
            "type": "integer"
        },
        "role_id": {
            "description": "A unique integer value identifying the role.",
            "in": "path",
            "name": "role_id",
            "required": true,
            "type": "integer"
        },
        "site_id": {
            "description": "A unique integer value identifying the site.",
            "in": "path",
            "name": "site_id",
            "required": true,
            "type": "integer"
        },
        "user_id": {
            "description": "A UUID value identifying the user.",
            "format": "uuid",
            "in": "path",
            "name": "user_id",
            "required": true,
            "type": "string"
        }
    },
    "paths": {
        "/adminnotes": {
            "get": {
                "operationId": "adminnote_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_user_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "description": "An optional query parameter to filter by creator (a user_id)",
                        "format": "uuid",
                        "in": "query",
                        "name": "creator_id",
                        "required": false,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/admin_note",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "adminnote_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/admin_note_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/admin_note",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "user_data"
                ]
            }
        },
        "/adminnotes/{admin_note_id}": {
            "delete": {
                "operationId": "adminnote_delete",
                "responses": {
                    "204": {
                        "description": "Deleted"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "get": {
                "operationId": "adminnote_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/admin_note",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/admin_note_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "adminnote_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/admin_note_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/admin_note",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "user_data"
                ]
            }
        },
        "/clients": {
            "get": {
                "operationId": "client_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of client ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "client_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    },
                    {
                        "description": "An optional client id to filter on. This is not the primary key.",
                        "in": "query",
                        "name": "client_id",
                        "required": false,
                        "type": "string"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/client",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "oidc_provider"
                ]
            }
        },
        "/clients/{client_id}": {
            "get": {
                "operationId": "client_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/client",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "oidc_provider"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/client_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/domainroles": {
            "get": {
                "operationId": "domainrole_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_domain_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/domain_role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "domainrole_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/domain_role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/domainroles/{domain_id}/{role_id}": {
            "delete": {
                "operationId": "domainrole_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "domainrole_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "domainrole_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/domain_role_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/domains": {
            "get": {
                "operationId": "domain_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of domain ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "domain_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/domain",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "domain_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/domain_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/domains/{domain_id}": {
            "delete": {
                "operationId": "domain_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "domain_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "domain_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/domain_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/invitationdomainroles": {
            "get": {
                "operationId": "invitationdomainrole_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_invitation_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_domain_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/invitation_domain_role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "invitationdomainrole_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/invitation_domain_role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation_domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/invitationdomainroles/{invitation_id}/{domain_id}/{role_id}": {
            "delete": {
                "operationId": "invitationdomainrole_delete",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "invitationdomainrole_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation_domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/invitation_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/invitations": {
            "get": {
                "operationId": "invitation_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "description": "Optional filter based on the invitor (the user who created the invitation)",
                        "format": "uuid",
                        "in": "query",
                        "name": "invitor_id",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of invitation ids",
                        "in": "query",
                        "items": {
                            "format": "uuid",
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "invitation_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/invitation",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "invitation_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/invitation_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/invitations/{invitation_id}": {
            "delete": {
                "operationId": "invitation_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "invitation_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/invitation_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "invitation_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/invitation_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/invitationsiteroles": {
            "get": {
                "operationId": "invitationsiterole_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_invitation_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_site_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/invitation_site_role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "invitationsiterole_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/invitation_site_role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation_site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/invitationsiteroles/{invitation_id}/{site_id}/{role_id}": {
            "delete": {
                "operationId": "invitationsiterole_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "invitationsiterole_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/invitation_site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/invitation_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/all_user_roles/{user_id}": {
            "get": {
                "description": "Get the effective roles that a user has at any place in the organisational tree.",
                "operationId": "get_all_user_roles",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/all_user_roles",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "User not found"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/domain_roles/{domain_id}": {
            "get": {
                "description": "Get the domain and its lineages roles defined for a domain.",
                "operationId": "get_domain_roles",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/domain_roles",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/site_and_domain_roles/{site_id}": {
            "get": {
                "description": "Get the site- and domain lineage roles defined for a given site.",
                "operationId": "get_site_and_domain_roles",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_and_domain_roles",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/site_role_labels_aggregated/{site_id}": {
            "get": {
                "description": "Get a list of all possible role labels that a user can have from the specified sites perspective.",
                "operationId": "get_site_role_labels_aggregated",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_role_labels_aggregated",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/user_site_role_labels_aggregated/{user_id}/{site_id}": {
            "get": {
                "description": "Get a list of all role labels that the specified user has from the specified sites perspective.",
                "operationId": "get_user_site_role_labels_aggregated",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_site_role_labels_aggregated",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/permissions": {
            "get": {
                "operationId": "permission_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of permission ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "permission_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/permission",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "permission_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/permission_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/permission",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/permissions/{permission_id}": {
            "delete": {
                "operationId": "permission_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "permission_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/permission",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/permission_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "permission_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/permission_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/permission",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/resources": {
            "get": {
                "operationId": "resource_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "description": "An optional URN prefix filter",
                        "in": "query",
                        "name": "prefix",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of resource ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "resource_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/resource",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "resource_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/resource_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/resource",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/resources/{resource_id}": {
            "delete": {
                "operationId": "resource_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "resource_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/resource",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/resource_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "resource_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/resource_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/resource",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/roleresourcepermissions": {
            "get": {
                "operationId": "roleresourcepermission_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "description": "An optional resource filter",
                        "in": "query",
                        "name": "resource_id",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "description": "An optional permission filter",
                        "in": "query",
                        "name": "permission_id",
                        "required": false,
                        "type": "integer"
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/role_resource_permission",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "roleresourcepermission_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/role_resource_permission_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/role_resource_permission",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/roleresourcepermissions/{role_id}/{resource_id}/{permission_id}": {
            "delete": {
                "operationId": "roleresourcepermission_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "roleresourcepermission_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/role_resource_permission",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/resource_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/permission_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/roles": {
            "get": {
                "operationId": "role_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of role ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "role_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "role_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/roles/{role_id}": {
            "delete": {
                "operationId": "role_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "role_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "role_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/role_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/sitedataschemas": {
            "get": {
                "operationId": "sitedataschema_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of site ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "site_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/site_data_schema",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "sitedataschema_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/site_data_schema_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_data_schema",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            }
        },
        "/sitedataschemas/{site_id}": {
            "delete": {
                "operationId": "sitedataschema_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "get": {
                "operationId": "sitedataschema_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_data_schema",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "sitedataschema_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/site_data_schema_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_data_schema",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            }
        },
        "/siteroles": {
            "get": {
                "operationId": "siterole_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_site_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/site_role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "siterole_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/site_role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/siteroles/{site_id}/{role_id}": {
            "delete": {
                "operationId": "siterole_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "siterole_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "siterole_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/site_role_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/sites": {
            "get": {
                "operationId": "site_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of site ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 0,
                        "name": "site_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/site",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "site_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/site_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/sites/{site_id}": {
            "delete": {
                "operationId": "site_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "site_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "site_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/site_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/site",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/sites/{site_id}/activate": {
            "get": {
                "description": "Activate the site so that users can log in to it.",
                "responses": {
                    "200": {
                        "description": "Site successfully activated"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Site not found"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/sites/{site_id}/deactivate": {
            "get": {
                "description": "Deactivate the site so that users cannot log in to it.",
                "responses": {
                    "200": {
                        "description": "Site successfully deactivated"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Site not found"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/userdomainroles": {
            "get": {
                "operationId": "userdomainrole_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_user_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_domain_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/user_domain_role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "userdomainrole_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/user_domain_role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/userdomainroles/{user_id}/{domain_id}/{role_id}": {
            "delete": {
                "operationId": "userdomainrole_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "userdomainrole_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_domain_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/users": {
            "get": {
                "operationId": "user_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "description": "An optional email filter",
                        "format": "email",
                        "in": "query",
                        "name": "email",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional username prefix filter",
                        "in": "query",
                        "name": "username_prefix",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "collectionFormat": "multi",
                        "description": "An optional list of user ids",
                        "in": "query",
                        "items": {
                            "format": "uuid",
                            "type": "string"
                        },
                        "minItems": 0,
                        "name": "user_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/user",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "oidc_provider"
                ]
            }
        },
        "/users/{user_id}": {
            "delete": {
                "operationId": "user_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "oidc_provider"
                ]
            },
            "get": {
                "operationId": "user_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "oidc_provider"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "user_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/user",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": ""
                    }
                },
                "tags": [
                    "oidc_provider"
                ]
            }
        },
        "/users/{user_id}/activate": {
            "get": {
                "description": "Activate the user account.",
                "responses": {
                    "200": {
                        "description": "Acccount successfully activated"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "User not found"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/users/{user_id}/deactivate": {
            "get": {
                "description": "Deactivate the user account.",
                "responses": {
                    "200": {
                        "description": "Acccount successfully deactivated"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "User not found"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/usersitedata": {
            "get": {
                "operationId": "usersitedata_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_user_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_site_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/user_site_data",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "usersitedata_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/user_site_data_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_site_data",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            }
        },
        "/usersitedata/{user_id}/{site_id}": {
            "delete": {
                "operationId": "usersitedata_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "get": {
                "operationId": "usersitedata_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_site_data",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "usersitedata_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/user_site_data_update",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_site_data",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "user_data"
                ]
            }
        },
        "/usersiteroles": {
            "get": {
                "operationId": "usersiterole_list",
                "parameters": [
                    {
                        "$ref": "#/parameters/optional_offset",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_limit",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_user_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_site_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "$ref": "#/parameters/optional_role_filter",
                        "x-scope": [
                            ""
                        ]
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/user_site_role",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "usersiterole_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/user_site_role_create",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            }
        },
        "/usersiteroles/{user_id}/{site_id}/{role_id}": {
            "delete": {
                "operationId": "usersiterole_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "get": {
                "operationId": "usersiterole_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/user_site_role",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "access_control"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/site_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/role_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        }
    },
    "schemes": [
        "http",
        "https"
    ],
    "security": [
        {
            "OAuth2": []
        },
        {
            "ApiKeyAuth": []
        }
    ],
    "securityDefinitions": {
        "ApiKeyAuth": {
            "description": "Workaround for lack of OIDC support. Use \\"Bearer id_token_goes_here\\" as the value.",
            "in": "header",
            "name": "Authorization",
            "type": "apiKey"
        },
        "OAuth2": {
            "authorizationUrl": "http://localhost:8000/openid/authorize",
            "flow": "accessCode",
            "scopes": {
                "address": "Addresses",
                "email": "Email",
                "openid": "Grants access to fields required by OpenID",
                "phone": "Phone numbers",
                "profile": "Profile fields",
                "roles": "Grants access to user roles",
                "site": "Grants access to site-specific data"
            },
            "tokenUrl": "http:///localhost:8000/openid/token",
            "type": "oauth2"
        }
    },
    "swagger": "2.0"
}""")

    async def get(self):
        """
        Override this function if further customisation to the spec is required.
        """
        # Mod spec to point to demo application
        spec = self.SPEC.copy()
        spec["basePath"] = "/"
        spec["host"] = "localhost:8000"
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["basic_auth"] = {"type": "basic"}
        spec["securityDefinitions"] = security_definitions
        return json_response(spec)
