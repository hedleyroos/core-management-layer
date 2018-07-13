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
from aiohttp_cors import CorsViewMixin

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


def maybe_validate_result(result, schema):
    if VALIDATE_RESPONSES:
        try:
            jsonschema.validate(result, schema)
        except ValidationError as e:
            LOGGER.error(e.message)


class Adminnotes(View, CorsViewMixin):

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
                "type": "string",
                "x-related-info": {
                    "label": "username",
                    "model": "user"
                }
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
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # user_id (optional): string An optional query parameter to filter by user_id
            user_id = self.request.query.get("user_id", None)
            if user_id is not None:
                jsonschema.validate(user_id, {"type": "string"})
                optional_args["user_id"] = user_id
            # creator_id (optional): string An optional query parameter to filter by creator (a user_id)
            creator_id = self.request.query.get("creator_id", None)
            if creator_id is not None:
                jsonschema.validate(creator_id, {"type": "string"})
                optional_args["creator_id"] = creator_id
            # admin_note_ids (optional): array An optional list of adminnote ids
            admin_note_ids = self.request.query.get("admin_note_ids", None)
            if admin_note_ids is not None:
                admin_note_ids = admin_note_ids.split(",")
            if admin_note_ids:
                admin_note_ids = [int(e) for e in admin_note_ids]
            if admin_note_ids is not None:
                schema = {'name': 'admin_note_ids', 'description': 'An optional list of adminnote ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(admin_note_ids, schema)
                optional_args["admin_note_ids"] = admin_note_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.adminnote_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class AdminnotesAdminNoteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Clients(View, CorsViewMixin):

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
                "type": "string",
                "x-related-info": {
                    "model": null
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # client_ids (optional): array An optional list of client ids
            client_ids = self.request.query.get("client_ids", None)
            if client_ids is not None:
                client_ids = client_ids.split(",")
            if client_ids:
                client_ids = [int(e) for e in client_ids]
            if client_ids is not None:
                schema = {'name': 'client_ids', 'description': 'An optional list of client ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(client_ids, schema)
                optional_args["client_ids"] = client_ids
            # client_token_id (optional): string An optional client id to filter on. This is not the primary key.
            client_token_id = self.request.query.get("client_token_id", None)
            if client_token_id is not None:
                jsonschema.validate(client_token_id, {"type": "string"})
                optional_args["client_token_id"] = client_token_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.client_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class ClientsClientId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.client

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A ClientsClientId instance
        """
        try:
            # client_id: integer A integer identifying the client
            client_id = self.request.match_info["client_id"]
            client_id = int(client_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.client_read(
            self.request, client_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Countries(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "code": {
                "maxLength": 2,
                "minLength": 2,
                "type": "string"
            },
            "name": {
                "maxLength": 100,
                "type": "string"
            }
        },
        "required": [
            "code",
            "name"
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
        :param self: A Countries instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # country_codes (optional): array An optional list of country codes
            country_codes = self.request.query.get("country_codes", None)
            if country_codes is not None:
                country_codes = country_codes.split(",")
            if country_codes is not None:
                schema = {'name': 'country_codes', 'description': 'An optional list of country codes', 'in': 'query', 'type': 'array', 'items': {'type': 'string', 'minLength': 2, 'maxLength': 2}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(country_codes, schema)
                optional_args["country_codes"] = country_codes
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.country_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class CountriesCountryCode(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.country

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A CountriesCountryCode instance
        """
        try:
            # country_code: string A unique two-character value identifying the country.
            country_code = self.request.match_info["country_code"]
            jsonschema.validate(country_code, {"type": "string"})
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.country_read(
            self.request, country_code, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Domainroles(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "grant_implicitly": {
                "type": "boolean"
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # domain_id (optional): integer An optional query parameter to filter by domain_id
            domain_id = self.request.query.get("domain_id", None)
            if domain_id is not None:
                domain_id = int(domain_id)
                optional_args["domain_id"] = domain_id
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domainrole_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class DomainrolesDomainIdRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Domains(View, CorsViewMixin):

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
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "domain"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # parent_id (optional): integer An optional query parameter to filter by parent_id
            parent_id = self.request.query.get("parent_id", None)
            if parent_id is not None:
                parent_id = int(parent_id)
                optional_args["parent_id"] = parent_id
            # domain_ids (optional): array An optional list of domain ids
            domain_ids = self.request.query.get("domain_ids", None)
            if domain_ids is not None:
                domain_ids = domain_ids.split(",")
            if domain_ids:
                domain_ids = [int(e) for e in domain_ids]
            if domain_ids is not None:
                schema = {'name': 'domain_ids', 'description': 'An optional list of domain ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(domain_ids, schema)
                optional_args["domain_ids"] = domain_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.domain_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class DomainsDomainId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Healthcheck(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.health_info

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Healthcheck instance
        """
        try:
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.healthcheck(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Invitationdomainroles(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "invitation_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "email"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # invitation_id (optional): string An optional query parameter to filter by invitation_id
            invitation_id = self.request.query.get("invitation_id", None)
            if invitation_id is not None:
                jsonschema.validate(invitation_id, {"type": "string"})
                optional_args["invitation_id"] = invitation_id
            # domain_id (optional): integer An optional query parameter to filter by domain_id
            domain_id = self.request.query.get("domain_id", None)
            if domain_id is not None:
                domain_id = int(domain_id)
                optional_args["domain_id"] = domain_id
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationdomainrole_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class InvitationdomainrolesInvitationIdDomainIdRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Invitations(View, CorsViewMixin):

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
                "readOnly": true,
                "type": "string",
                "x-related-info": {
                    "label": "username",
                    "model": "user"
                }
            },
            "last_name": {
                "maxLength": 100,
                "type": "string"
            },
            "organisation_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "organisation"
                }
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
            "organisation_id",
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # invitor_id (optional): string Optional filter based on the invitor (the user who created the invitation)
            invitor_id = self.request.query.get("invitor_id", None)
            if invitor_id is not None:
                jsonschema.validate(invitor_id, {"type": "string"})
                optional_args["invitor_id"] = invitor_id
            # invitation_ids (optional): array An optional list of invitation ids
            invitation_ids = self.request.query.get("invitation_ids", None)
            if invitation_ids is not None:
                invitation_ids = invitation_ids.split(",")
            if invitation_ids:
                invitation_ids = [int(e) for e in invitation_ids]
            if invitation_ids is not None:
                schema = {'name': 'invitation_ids', 'description': 'An optional list of invitation ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer', 'format': 'uuid'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(invitation_ids, schema)
                optional_args["invitation_ids"] = invitation_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitation_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class InvitationsInvitationId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Invitationsiteroles(View, CorsViewMixin):

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
                "type": "string",
                "x-related-info": {
                    "label": "email"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # invitation_id (optional): string An optional query parameter to filter by invitation_id
            invitation_id = self.request.query.get("invitation_id", None)
            if invitation_id is not None:
                jsonschema.validate(invitation_id, {"type": "string"})
                optional_args["invitation_id"] = invitation_id
            # site_id (optional): integer An optional query parameter to filter by site_id
            site_id = self.request.query.get("site_id", None)
            if site_id is not None:
                site_id = int(site_id)
                optional_args["site_id"] = site_id
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.invitationsiterole_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class InvitationsiterolesInvitationIdSiteIdRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsAllUserRolesUserId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsDomainRolesDomainId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsGetSiteFromClientTokenIdClientTokenId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.site

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsGetSiteFromClientTokenIdClientTokenId instance
        """
        try:
            # client_token_id: string A client token id. This is not the primary key of the client table, but rather the client id that is typically configured along with the client secret.
            client_token_id = self.request.match_info["client_token_id"]
            jsonschema.validate(client_token_id, {"type": "string"})
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_site_from_client_token_id(
            self.request, client_token_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsGetSitesUnderDomainDomainId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "client_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsGetSitesUnderDomainDomainId instance
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

        result = await Stubs.get_sites_under_domain(
            self.request, domain_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsSiteAndDomainRolesSiteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsSiteRoleLabelsAggregatedSiteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUserDomainPermissionsUserIdDomainId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "type": "string"
    },
    "type": "array",
    "uniqueItems": true
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsUserDomainPermissionsUserIdDomainId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # domain_id: integer A unique integer value identifying the domain.
            domain_id = self.request.match_info["domain_id"]
            domain_id = int(domain_id)
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_user_domain_permissions(
            self.request, user_id, domain_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUserHasPermissionsUserId(View, CorsViewMixin):

    POST_RESPONSE_SCHEMA = schemas.user_permissions_check_response
    POST_BODY_SCHEMA = schemas.user_permissions_check

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsUserHasPermissionsUserId instance
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

            jsonschema.validate(body, schema=self.POST_BODY_SCHEMA)
        except ValidationError as ve:
            return Response(status=400, text="Body validation failed: {}".format(ve.message))
        except Exception:
            return Response(status=400, text="JSON body expected")

        result = await Stubs.user_has_permissions(
            self.request, body, user_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUserManagementPortalPermissionsUserId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "type": "string"
    },
    "type": "array",
    "uniqueItems": true
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsUserManagementPortalPermissionsUserId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_user_management_portal_permissions(
            self.request, user_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUserSitePermissionsUserIdSiteId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "type": "string"
    },
    "type": "array",
    "uniqueItems": true
}""")

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OpsUserSitePermissionsUserIdSiteId instance
        """
        try:
            # user_id: string A UUID value identifying the user.
            user_id = self.request.match_info["user_id"]
            jsonschema.validate(user_id, {"type": "string"})
            # site_id: integer A unique integer value identifying the site.
            site_id = self.request.match_info["site_id"]
            site_id = int(site_id)
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.get_user_site_permissions(
            self.request, user_id, site_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUserSiteRoleLabelsAggregatedUserIdSiteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUsersWithRolesForDomainDomainId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "description": "A user with their roles.",
        "properties": {
            "id": {
                "format": "uuid",
                "type": "string"
            },
            "roles": {
                "items": {
                    "type": "string"
                },
                "type": "array"
            },
            "username": {
                "type": "string"
            }
        },
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
        :param self: A OpsUsersWithRolesForDomainDomainId instance
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

        result = await Stubs.get_users_with_roles_for_domain(
            self.request, domain_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class OpsUsersWithRolesForSiteSiteId(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "description": "A user with their roles.",
        "properties": {
            "id": {
                "format": "uuid",
                "type": "string"
            },
            "roles": {
                "items": {
                    "type": "string"
                },
                "type": "array"
            },
            "username": {
                "type": "string"
            }
        },
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
        :param self: A OpsUsersWithRolesForSiteSiteId instance
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

        result = await Stubs.get_users_with_roles_for_site(
            self.request, site_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Organisations(View, CorsViewMixin):

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
                "type": "integer"
            },
            "name": {
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
            "description",
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
    POST_RESPONSE_SCHEMA = schemas.organisation
    POST_BODY_SCHEMA = schemas.organisation_create

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Organisations instance
        """
        try:
            optional_args = {}
            # offset (optional): integer An optional query parameter specifying the offset in the result set to start from.
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # organisation_ids (optional): array An optional list of organisation ids
            organisation_ids = self.request.query.get("organisation_ids", None)
            if organisation_ids is not None:
                organisation_ids = organisation_ids.split(",")
            if organisation_ids:
                organisation_ids = [int(e) for e in organisation_ids]
            if organisation_ids is not None:
                schema = {'name': 'organisation_ids', 'description': 'An optional list of organisation ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(organisation_ids, schema)
                optional_args["organisation_ids"] = organisation_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.organisation_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

    async def post(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A Organisations instance
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

        result = await Stubs.organisation_create(
            self.request, body, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class OrganisationsOrganisationId(View, CorsViewMixin):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.organisation
    PUT_RESPONSE_SCHEMA = schemas.organisation
    PUT_BODY_SCHEMA = schemas.organisation_update

    async def delete(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OrganisationsOrganisationId instance
        """
        try:
            # organisation_id: integer An integer identifying an organisation
            organisation_id = self.request.match_info["organisation_id"]
            organisation_id = int(organisation_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.organisation_delete(
            self.request, organisation_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.DELETE_RESPONSE_SCHEMA)

        return HTTPNoContent()

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OrganisationsOrganisationId instance
        """
        try:
            # organisation_id: integer An integer identifying an organisation
            organisation_id = self.request.match_info["organisation_id"]
            organisation_id = int(organisation_id)
            optional_args = {}
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.organisation_read(
            self.request, organisation_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

    async def put(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A OrganisationsOrganisationId instance
        """
        try:
            # organisation_id: integer An integer identifying an organisation
            organisation_id = self.request.match_info["organisation_id"]
            organisation_id = int(organisation_id)
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

        result = await Stubs.organisation_update(
            self.request, body, organisation_id, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Permissions(View, CorsViewMixin):

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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # permission_ids (optional): array An optional list of permission ids
            permission_ids = self.request.query.get("permission_ids", None)
            if permission_ids is not None:
                permission_ids = permission_ids.split(",")
            if permission_ids:
                permission_ids = [int(e) for e in permission_ids]
            if permission_ids is not None:
                schema = {'name': 'permission_ids', 'description': 'An optional list of permission ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(permission_ids, schema)
                optional_args["permission_ids"] = permission_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.permission_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class PermissionsPermissionId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshAll(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshAll instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_all(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshClients(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshClients instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_clients(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshDomains(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshDomains instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_domains(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshKeys(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshKeys instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_keys(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshPermissions(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshPermissions instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_permissions(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshResources(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshResources instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_resources(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshRoles(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshRoles instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_roles(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class RefreshSites(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__

    async def get(self):
        """
        No parameters are passed explicitly. We unpack it from the request.
        :param self: A RefreshSites instance
        """
        try:
            optional_args = {}
            # nocache (optional): boolean An optional query parameter to instructing an API call to by pass caches when reading data.
            nocache = self.request.query.get("nocache", None)
            if nocache is not None:
                nocache = (nocache.lower() == "true")
                jsonschema.validate(nocache, {"type": "boolean"})
                optional_args["nocache"] = nocache
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.refresh_sites(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Resources(View, CorsViewMixin):

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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # prefix (optional): string An optional URN prefix filter
            prefix = self.request.query.get("prefix", None)
            if prefix is not None:
                jsonschema.validate(prefix, {"type": "string"})
                optional_args["prefix"] = prefix
            # resource_ids (optional): array An optional list of resource ids
            resource_ids = self.request.query.get("resource_ids", None)
            if resource_ids is not None:
                resource_ids = resource_ids.split(",")
            if resource_ids:
                resource_ids = [int(e) for e in resource_ids]
            if resource_ids is not None:
                schema = {'name': 'resource_ids', 'description': 'An optional list of resource ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(resource_ids, schema)
                optional_args["resource_ids"] = resource_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.resource_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class ResourcesResourceId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Roleresourcepermissions(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "permission_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "resource_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "urn"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
            # resource_id (optional): integer An optional resource filter
            resource_id = self.request.query.get("resource_id", None)
            if resource_id is not None:
                resource_id = int(resource_id)
                optional_args["resource_id"] = resource_id
            # permission_id (optional): integer An optional permission filter
            permission_id = self.request.query.get("permission_id", None)
            if permission_id is not None:
                permission_id = int(permission_id)
                optional_args["permission_id"] = permission_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.roleresourcepermission_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class RoleresourcepermissionsRoleIdResourceIdPermissionId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Roles(View, CorsViewMixin):

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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # role_ids (optional): array An optional list of role ids
            role_ids = self.request.query.get("role_ids", None)
            if role_ids is not None:
                role_ids = role_ids.split(",")
            if role_ids:
                role_ids = [int(e) for e in role_ids]
            if role_ids is not None:
                schema = {'name': 'role_ids', 'description': 'An optional list of role ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(role_ids, schema)
                optional_args["role_ids"] = role_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.role_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class RolesRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Sitedataschemas(View, CorsViewMixin):

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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # site_ids (optional): array An optional list of site ids
            site_ids = self.request.query.get("site_ids", None)
            if site_ids is not None:
                site_ids = site_ids.split(",")
            if site_ids:
                site_ids = [int(e) for e in site_ids]
            if site_ids is not None:
                schema = {'name': 'site_ids', 'description': 'An optional list of site ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(site_ids, schema)
                optional_args["site_ids"] = site_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.sitedataschema_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class SitedataschemasSiteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Siteroles(View, CorsViewMixin):

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
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # site_id (optional): integer An optional query parameter to filter by site_id
            site_id = self.request.query.get("site_id", None)
            if site_id is not None:
                site_id = int(site_id)
                optional_args["site_id"] = site_id
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.siterole_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class SiterolesSiteIdRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Sites(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "client_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # site_ids (optional): array An optional list of site ids
            site_ids = self.request.query.get("site_ids", None)
            if site_ids is not None:
                site_ids = site_ids.split(",")
            if site_ids:
                site_ids = [int(e) for e in site_ids]
            if site_ids is not None:
                schema = {'name': 'site_ids', 'description': 'An optional list of site ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(site_ids, schema)
                optional_args["site_ids"] = site_ids
            # client_id (optional): integer An optional client id to filter on
            client_id = self.request.query.get("client_id", None)
            if client_id is not None:
                client_id = int(client_id)
                optional_args["client_id"] = client_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.site_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class SitesSiteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class SitesSiteIdActivate(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class SitesSiteIdDeactivate(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Userdomainroles(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "domain_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # user_id (optional): string An optional query parameter to filter by user_id
            user_id = self.request.query.get("user_id", None)
            if user_id is not None:
                jsonschema.validate(user_id, {"type": "string"})
                optional_args["user_id"] = user_id
            # domain_id (optional): integer An optional query parameter to filter by domain_id
            domain_id = self.request.query.get("domain_id", None)
            if domain_id is not None:
                domain_id = int(domain_id)
                optional_args["domain_id"] = domain_id
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.userdomainrole_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class UserdomainrolesUserIdDomainIdRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Users(View, CorsViewMixin):

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
                "minLength": 2,
                "type": "string",
                "x-related-info": {
                    "field": "code",
                    "label": "name",
                    "model": "country"
                }
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
                "format": "date-time",
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
            "organisation_id": {
                "readOnly": true,
                "type": "integer",
                "x-related-info": {
                    "label": "name",
                    "model": "organisation"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # birth_date (optional): string An optional birth_date range filter
            birth_date = self.request.query.get("birth_date", None)
            if birth_date is not None:
                jsonschema.validate(birth_date, {"type": "string"})
                optional_args["birth_date"] = birth_date
            # country (optional): string An optional country filter
            country = self.request.query.get("country", None)
            if country is not None:
                jsonschema.validate(country, {"type": "string"})
                optional_args["country"] = country
            # date_joined (optional): string An optional date joined range filter
            date_joined = self.request.query.get("date_joined", None)
            if date_joined is not None:
                jsonschema.validate(date_joined, {"type": "string"})
                optional_args["date_joined"] = date_joined
            # email (optional): string An optional case insensitive email inner match filter
            email = self.request.query.get("email", None)
            if email is not None:
                jsonschema.validate(email, {"type": "string"})
                optional_args["email"] = email
            # email_verified (optional): boolean An optional email verified filter
            email_verified = self.request.query.get("email_verified", None)
            if email_verified is not None:
                email_verified = (email_verified.lower() == "true")
                jsonschema.validate(email_verified, {"type": "boolean"})
                optional_args["email_verified"] = email_verified
            # first_name (optional): string An optional case insensitive first name inner match filter
            first_name = self.request.query.get("first_name", None)
            if first_name is not None:
                jsonschema.validate(first_name, {"type": "string"})
                optional_args["first_name"] = first_name
            # gender (optional): string An optional gender filter
            gender = self.request.query.get("gender", None)
            if gender is not None:
                jsonschema.validate(gender, {"type": "string"})
                optional_args["gender"] = gender
            # is_active (optional): boolean An optional is_active filter
            is_active = self.request.query.get("is_active", None)
            if is_active is not None:
                is_active = (is_active.lower() == "true")
                jsonschema.validate(is_active, {"type": "boolean"})
                optional_args["is_active"] = is_active
            # last_login (optional): string An optional last login range filter
            last_login = self.request.query.get("last_login", None)
            if last_login is not None:
                jsonschema.validate(last_login, {"type": "string"})
                optional_args["last_login"] = last_login
            # last_name (optional): string An optional case insensitive last name inner match filter
            last_name = self.request.query.get("last_name", None)
            if last_name is not None:
                jsonschema.validate(last_name, {"type": "string"})
                optional_args["last_name"] = last_name
            # msisdn (optional): string An optional case insensitive MSISDN inner match filter
            msisdn = self.request.query.get("msisdn", None)
            if msisdn is not None:
                jsonschema.validate(msisdn, {"type": "string"})
                optional_args["msisdn"] = msisdn
            # msisdn_verified (optional): boolean An optional MSISDN verified filter
            msisdn_verified = self.request.query.get("msisdn_verified", None)
            if msisdn_verified is not None:
                msisdn_verified = (msisdn_verified.lower() == "true")
                jsonschema.validate(msisdn_verified, {"type": "boolean"})
                optional_args["msisdn_verified"] = msisdn_verified
            # nickname (optional): string An optional case insensitive nickname inner match filter
            nickname = self.request.query.get("nickname", None)
            if nickname is not None:
                jsonschema.validate(nickname, {"type": "string"})
                optional_args["nickname"] = nickname
            # organisation_id (optional): integer An optional filter on the organisation id
            organisation_id = self.request.query.get("organisation_id", None)
            if organisation_id is not None:
                organisation_id = int(organisation_id)
                optional_args["organisation_id"] = organisation_id
            # updated_at (optional): string An optional updated_at range filter
            updated_at = self.request.query.get("updated_at", None)
            if updated_at is not None:
                jsonschema.validate(updated_at, {"type": "string"})
                optional_args["updated_at"] = updated_at
            # username (optional): string An optional case insensitive username inner match filter
            username = self.request.query.get("username", None)
            if username is not None:
                jsonschema.validate(username, {"type": "string"})
                optional_args["username"] = username
            # q (optional): string An optional case insensitive inner match filter across all searchable text fields
            q = self.request.query.get("q", None)
            if q is not None:
                jsonschema.validate(q, {"type": "string"})
                optional_args["q"] = q
            # tfa_enabled (optional): boolean An optional filter based on whether a user has 2FA enabled or not
            tfa_enabled = self.request.query.get("tfa_enabled", None)
            if tfa_enabled is not None:
                tfa_enabled = (tfa_enabled.lower() == "true")
                jsonschema.validate(tfa_enabled, {"type": "boolean"})
                optional_args["tfa_enabled"] = tfa_enabled
            # has_organisation (optional): boolean An optional filter based on whether a user belongs to an organisation or not
            has_organisation = self.request.query.get("has_organisation", None)
            if has_organisation is not None:
                has_organisation = (has_organisation.lower() == "true")
                jsonschema.validate(has_organisation, {"type": "boolean"})
                optional_args["has_organisation"] = has_organisation
            # order_by (optional): array Fields and directions to order by, e.g. "-created_at,username". Add "-" in front of a field name to indicate descending order.
            order_by = self.request.query.get("order_by", None)
            if order_by is not None:
                order_by = order_by.split(",")
            if order_by is not None:
                schema = {'name': 'order_by', 'description': 'Fields and directions to order by, e.g. "-created_at,username". Add "-" in front of a field name to indicate descending order.', 'in': 'query', 'required': False, 'type': 'array', 'collectionFormat': 'csv', 'items': {'type': 'string'}, 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(order_by, schema)
                optional_args["order_by"] = order_by
            # user_ids (optional): array An optional list of user ids
            user_ids = self.request.query.get("user_ids", None)
            if user_ids is not None:
                user_ids = user_ids.split(",")
            if user_ids is not None:
                schema = {'name': 'user_ids', 'description': 'An optional list of user ids', 'in': 'query', 'type': 'array', 'items': {'type': 'string', 'format': 'uuid'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(user_ids, schema)
                optional_args["user_ids"] = user_ids
            # site_ids (optional): array An optional list of site ids
            site_ids = self.request.query.get("site_ids", None)
            if site_ids is not None:
                site_ids = site_ids.split(",")
            if site_ids:
                site_ids = [int(e) for e in site_ids]
            if site_ids is not None:
                schema = {'name': 'site_ids', 'description': 'An optional list of site ids', 'in': 'query', 'type': 'array', 'items': {'type': 'integer'}, 'required': False, 'minItems': 1, 'collectionFormat': 'csv', 'uniqueItems': True, 'x-related-info': {'rest_resource_name': 'sites', 'label': 'name'}}
                # Remove Swagger fields that clash with JSONSchema names at this level
                for field in ["name", "in", "required", "collectionFormat"]:
                    if field in schema:
                        del schema[field]

                jsonschema.validate(site_ids, schema)
                optional_args["site_ids"] = site_ids
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.user_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UsersUserId(View, CorsViewMixin):

    DELETE_RESPONSE_SCHEMA = schemas.__UNSPECIFIED__
    GET_RESPONSE_SCHEMA = schemas.user
    PUT_RESPONSE_SCHEMA = schemas.user
    PUT_BODY_SCHEMA = schemas.user_update

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UsersUserIdActivate(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class UsersUserIdDeactivate(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Usersitedata(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "data": {
                "type": "object"
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
            }
        },
        "required": [
            "user_id",
            "site_id",
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # user_id (optional): string An optional query parameter to filter by user_id
            user_id = self.request.query.get("user_id", None)
            if user_id is not None:
                jsonschema.validate(user_id, {"type": "string"})
                optional_args["user_id"] = user_id
            # site_id (optional): integer An optional query parameter to filter by site_id
            site_id = self.request.query.get("site_id", None)
            if site_id is not None:
                site_id = int(site_id)
                optional_args["site_id"] = site_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersitedata_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class UsersitedataUserIdSiteId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.PUT_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class Usersiteroles(View, CorsViewMixin):

    GET_RESPONSE_SCHEMA = json.loads("""{
    "items": {
        "properties": {
            "created_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "role_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "label"
                }
            },
            "site_id": {
                "type": "integer",
                "x-related-info": {
                    "label": "name"
                }
            },
            "updated_at": {
                "format": "date-time",
                "readOnly": true,
                "type": "string"
            },
            "user_id": {
                "format": "uuid",
                "type": "string",
                "x-related-info": {
                    "label": "username"
                }
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
            offset = self.request.query.get("offset", None)
            if offset is not None:
                offset = int(offset)
                if offset < 0:
                    raise ValidationError("offset exceeds its minimum limit")
                optional_args["offset"] = offset
            # limit (optional): integer An optional query parameter to limit the number of results returned.
            limit = self.request.query.get("limit", None)
            if limit is not None:
                limit = int(limit)
                if limit < 1:
                    raise ValidationError("limit exceeds its minimum limit")
                if 100 < limit:
                    raise ValidationError("limit exceeds its maximum limit")
                optional_args["limit"] = limit
            # user_id (optional): string An optional query parameter to filter by user_id
            user_id = self.request.query.get("user_id", None)
            if user_id is not None:
                jsonschema.validate(user_id, {"type": "string"})
                optional_args["user_id"] = user_id
            # site_id (optional): integer An optional query parameter to filter by site_id
            site_id = self.request.query.get("site_id", None)
            if site_id is not None:
                site_id = int(site_id)
                optional_args["site_id"] = site_id
            # role_id (optional): integer An optional query parameter to filter by role_id
            role_id = self.request.query.get("role_id", None)
            if role_id is not None:
                role_id = int(role_id)
                optional_args["role_id"] = role_id
        except ValidationError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve.message))
        except ValueError as ve:
            return Response(status=400, text="Parameter validation failed: {}".format(ve))

        result = await Stubs.usersiterole_list(
            self.request, **optional_args)

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.POST_RESPONSE_SCHEMA)

        return json_response(result, status=201, headers=headers)


class UsersiterolesUserIdSiteIdRoleId(View, CorsViewMixin):

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

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

        if type(result) is tuple:
            result, headers = result
        else:
            headers = {}

        maybe_validate_result(result, self.GET_RESPONSE_SCHEMA)

        return json_response(result, headers=headers)


class __SWAGGER_SPEC__(View, CorsViewMixin):
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
                    "type": "string",
                    "x-related-info": {
                        "label": "username",
                        "model": "user"
                    }
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
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
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
                    "type": "string",
                    "x-related-info": {
                        "label": "username",
                        "model": "user"
                    }
                },
                "note": {
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
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
                    "type": "string",
                    "x-related-info": {
                        "model": null
                    }
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
        "country": {
            "properties": {
                "code": {
                    "maxLength": 2,
                    "minLength": 2,
                    "type": "string"
                },
                "name": {
                    "maxLength": 100,
                    "type": "string"
                }
            },
            "required": [
                "code",
                "name"
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "domain"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "domain"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "grant_implicitly": {
                    "type": "boolean"
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "grant_implicitly": {
                    "type": "boolean"
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "domain"
                    }
                }
            },
            "type": "object"
        },
        "health_info": {
            "description": "Health check response",
            "properties": {
                "access_control_health": {
                    "type": "object"
                },
                "authentication_service_health": {
                    "type": "object"
                },
                "host": {
                    "type": "string"
                },
                "server_timestamp": {
                    "format": "date-time",
                    "type": "string"
                },
                "user_data_store_health": {
                    "type": "object"
                },
                "version": {
                    "type": "string"
                }
            },
            "required": [
                "host",
                "server_timestamp",
                "version",
                "access_control_health",
                "user_data_store_health",
                "authentication_service_health"
            ],
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
                    "readOnly": true,
                    "type": "string",
                    "x-related-info": {
                        "label": "username",
                        "model": "user"
                    }
                },
                "last_name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "organisation_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "organisation"
                    }
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
                "organisation_id",
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
                "last_name": {
                    "maxLength": 100,
                    "type": "string"
                },
                "organisation_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "organisation"
                    }
                }
            },
            "required": [
                "first_name",
                "last_name",
                "email",
                "organisation_id"
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "invitation_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "email"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "invitation_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "email"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
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
                    "type": "string",
                    "x-related-info": {
                        "label": "email"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "string",
                    "x-related-info": {
                        "label": "email"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                },
                "organisation_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "organisation"
                    }
                }
            },
            "type": "object"
        },
        "organisation": {
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
                    "type": "integer"
                },
                "name": {
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
                "description",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "organisation_create": {
            "properties": {
                "description": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                }
            },
            "required": [
                "name"
            ],
            "type": "object"
        },
        "organisation_update": {
            "minProperties": 1,
            "properties": {
                "description": {
                    "type": "string"
                },
                "name": {
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
        "resource_permission": {
            "properties": {
                "permission": {
                    "type": "string"
                },
                "resource": {
                    "format": "uri",
                    "type": "string"
                }
            },
            "required": [
                "resource",
                "permission"
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
                    "default": true,
                    "type": "boolean"
                }
            },
            "required": [
                "label"
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "resource_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "urn"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "resource_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "urn"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    },
                    "type": "object"
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "description": {
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "description": {
                    "type": "string"
                },
                "domain_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
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
                    "minLength": 2,
                    "type": "string",
                    "x-related-info": {
                        "field": "code",
                        "label": "name",
                        "model": "country"
                    }
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
                    "format": "date-time",
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
                "organisation_id": {
                    "readOnly": true,
                    "type": "integer",
                    "x-related-info": {
                        "label": "name",
                        "model": "organisation"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "role_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
                }
            },
            "required": [
                "user_id",
                "domain_id",
                "role_id"
            ],
            "type": "object"
        },
        "user_permissions_check": {
            "properties": {
                "domain_id": {
                    "type": "integer"
                },
                "nocache": {
                    "default": false,
                    "type": "boolean"
                },
                "operator": {
                    "enum": [
                        "all",
                        "any"
                    ],
                    "type": "string"
                },
                "resource_permissions": {
                    "items": {
                        "$ref": "#/definitions/resource_permission",
                        "x-scope": [
                            "",
                            "#/definitions/user_permissions_check"
                        ]
                    },
                    "type": "array"
                },
                "site_id": {
                    "type": "integer"
                }
            },
            "required": [
                "operator",
                "resource_permissions"
            ],
            "type": "object"
        },
        "user_permissions_check_response": {
            "properties": {
                "has_permissions": {
                    "type": "boolean"
                }
            },
            "required": [
                "has_permissions"
            ],
            "type": "object"
        },
        "user_site_data": {
            "properties": {
                "created_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "data": {
                    "type": "object"
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
                }
            },
            "required": [
                "user_id",
                "site_id",
                "data",
                "created_at",
                "updated_at"
            ],
            "type": "object"
        },
        "user_site_data_create": {
            "properties": {
                "data": {
                    "type": "object"
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "updated_at": {
                    "format": "date-time",
                    "readOnly": true,
                    "type": "string"
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
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
                    "type": "integer",
                    "x-related-info": {
                        "label": "label"
                    }
                },
                "site_id": {
                    "type": "integer",
                    "x-related-info": {
                        "label": "name"
                    }
                },
                "user_id": {
                    "format": "uuid",
                    "type": "string",
                    "x-related-info": {
                        "label": "username"
                    }
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
                    "minLength": 2,
                    "type": "string",
                    "x-related-info": {
                        "field": "code",
                        "label": "name",
                        "model": "country"
                    }
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
        },
        "user_with_roles": {
            "description": "A user with their roles.",
            "properties": {
                "id": {
                    "format": "uuid",
                    "type": "string"
                },
                "roles": {
                    "items": {
                        "type": "string"
                    },
                    "type": "array"
                },
                "username": {
                    "type": "string"
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
            "description": "A integer identifying the client",
            "in": "path",
            "name": "client_id",
            "required": true,
            "type": "integer"
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
            "type": "integer",
            "x-related-info": {
                "label": "name",
                "rest_resource_name": "domains"
            }
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
            "type": "integer",
            "x-admin-on-rest-exclude": true
        },
        "optional_nocache": {
            "default": false,
            "description": "An optional query parameter to instructing an API call to by pass caches when reading data.",
            "in": "query",
            "name": "nocache",
            "required": false,
            "type": "boolean"
        },
        "optional_offset": {
            "default": 0,
            "description": "An optional query parameter specifying the offset in the result set to start from.",
            "in": "query",
            "minimum": 0,
            "name": "offset",
            "required": false,
            "type": "integer",
            "x-admin-on-rest-exclude": true
        },
        "optional_parent_filter": {
            "description": "An optional query parameter to filter by parent_id",
            "in": "query",
            "name": "parent_id",
            "required": false,
            "type": "integer",
            "x-related-info": {
                "label": "name",
                "rest_resource_name": "domains"
            }
        },
        "optional_portal_context_header": {
            "in": "header",
            "name": "X-GE-Portal-Context",
            "required": false,
            "type": "string"
        },
        "optional_role_filter": {
            "description": "An optional query parameter to filter by role_id",
            "in": "query",
            "name": "role_id",
            "required": false,
            "type": "integer",
            "x-related-info": {
                "label": "label",
                "rest_resource_name": "roles"
            }
        },
        "optional_site_filter": {
            "description": "An optional query parameter to filter by site_id",
            "in": "query",
            "name": "site_id",
            "required": false,
            "type": "integer",
            "x-related-info": {
                "label": "name",
                "rest_resource_name": "sites"
            }
        },
        "optional_user_filter": {
            "description": "An optional query parameter to filter by user_id",
            "format": "uuid",
            "in": "query",
            "name": "user_id",
            "required": false,
            "type": "string"
        },
        "organisation_id": {
            "description": "An integer identifying an organisation",
            "in": "path",
            "name": "organisation_id",
            "required": true,
            "type": "integer"
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
                    },
                    {
                        "collectionFormat": "csv",
                        "description": "An optional list of adminnote ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
                        "name": "admin_note_ids",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:adminnote:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:adminnote:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:adminnote:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:adminnote:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:adminnote:update"
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
                        "collectionFormat": "csv",
                        "description": "An optional list of client ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
                        "name": "client_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    },
                    {
                        "description": "An optional client id to filter on. This is not the primary key.",
                        "in": "query",
                        "name": "client_token_id",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:oidc_provider:client:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ]
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
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:oidc_provider:client:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/client_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/countries": {
            "get": {
                "operationId": "country_list",
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
                        "collectionFormat": "csv",
                        "description": "An optional list of country codes",
                        "in": "query",
                        "items": {
                            "maxLength": 2,
                            "minLength": 2,
                            "type": "string"
                        },
                        "minItems": 1,
                        "name": "country_codes",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/country",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "authentication"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/countries/{country_code}": {
            "get": {
                "operationId": "country_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/country",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "authentication"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/country_code",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domainrole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domainrole:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domainrole:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domainrole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domainrole:update"
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
                        "$ref": "#/parameters/optional_parent_filter",
                        "x-scope": [
                            ""
                        ]
                    },
                    {
                        "collectionFormat": "csv",
                        "description": "An optional list of domain ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domain:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domain:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domain:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domain:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:domain:update"
                ]
            }
        },
        "/healthcheck": {
            "get": {
                "description": "Get the status of the service.",
                "operationId": "healthcheck",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "The service is operating normally.",
                        "schema": {
                            "$ref": "#/definitions/health_info",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "security": []
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationdomainrole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationdomainrole:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationdomainrole:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationdomainrole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                        "collectionFormat": "csv",
                        "description": "An optional list of invitation ids",
                        "in": "query",
                        "items": {
                            "format": "uuid",
                            "type": "integer"
                        },
                        "minItems": 1,
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitation:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitation:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitation:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitation:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitation:update"
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationsiterole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationsiterole:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationsiterole:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:invitationsiterole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/get_site_from_client_token_id/{client_token_id}": {
            "get": {
                "description": "Get the site associated with the specified client token id",
                "operationId": "get_site_from_client_token_id",
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "description": "A client token id. This is not the primary key of the client table, but rather the client id that is typically configured along with the client secret.",
                    "in": "path",
                    "name": "client_token_id",
                    "required": true,
                    "type": "string"
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/get_sites_under_domain/{domain_id}": {
            "get": {
                "description": "Get a list of all sites linked directly or indirectly to the specified domain.",
                "operationId": "get_sites_under_domain",
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
                    "$ref": "#/parameters/optional_portal_context_header",
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
                    "$ref": "#/parameters/optional_portal_context_header",
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
        "/ops/user_domain_permissions/{user_id}/{domain_id}": {
            "get": {
                "description": "Get a list of all resource permissions a user has on the specified domain",
                "operationId": "get_user_domain_permissions",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array",
                            "uniqueItems": true
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/user_has_permissions/{user_id}": {
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "in": "body",
                    "name": "data",
                    "schema": {
                        "$ref": "#/definitions/user_permissions_check",
                        "x-scope": [
                            ""
                        ]
                    }
                }
            ],
            "post": {
                "consumes": [
                    "application/json"
                ],
                "description": "Check of the user has the specified resource permissions",
                "operationId": "user_has_permissions",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "True if the user has the permissions, else False",
                        "schema": {
                            "$ref": "#/definitions/user_permissions_check_response",
                            "x-scope": [
                                ""
                            ]
                        }
                    },
                    "400": {
                        "description": "Bad Request"
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
            }
        },
        "/ops/user_management_portal_permissions/{user_id}": {
            "get": {
                "deprecated": true,
                "description": "(DEPRECATED. Use /ops/user_site_permissions instead.) Get a list of all permissions a user has on the Management Portal",
                "operationId": "get_user_management_portal_permissions",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array",
                            "uniqueItems": true
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/user_id",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/user_site_permissions/{user_id}/{site_id}": {
            "get": {
                "description": "Get a list of all resource permissions a user has on the specified site",
                "operationId": "get_user_site_permissions",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "type": "string"
                            },
                            "type": "array",
                            "uniqueItems": true
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                    "$ref": "#/parameters/optional_nocache",
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
        "/ops/users_with_roles_for_domain/{domain_id}": {
            "get": {
                "description": "Get a list of Users with their effective roles within the given domain.",
                "operationId": "get_users_with_roles_for_domain",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/user_with_roles",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Domain not found"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/domain_id",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/ops/users_with_roles_for_site/{site_id}": {
            "get": {
                "description": "Get a list of Users with their effective roles within the given site.",
                "operationId": "get_users_with_roles_for_site",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/user_with_roles",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Site not found"
                    }
                },
                "tags": [
                    "operational"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
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
        "/organisations": {
            "get": {
                "operationId": "organisation_list",
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
                        "collectionFormat": "csv",
                        "description": "An optional list of organisation ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
                        "name": "organisation_ids",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
                        "schema": {
                            "items": {
                                "$ref": "#/definitions/organisation",
                                "x-scope": [
                                    ""
                                ]
                            },
                            "type": "array"
                        }
                    }
                },
                "tags": [
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:organisation:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "post": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "organisation_create",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/organisation_create",
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
                            "$ref": "#/definitions/organisation",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:organisation:create"
                ]
            }
        },
        "/organisations/{organisation_id}": {
            "delete": {
                "operationId": "organisation_delete",
                "responses": {
                    "204": {
                        "description": ""
                    }
                },
                "tags": [
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:organisation:delete"
                ]
            },
            "get": {
                "operationId": "organisation_read",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/organisation",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:organisation:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/organisation_id",
                    "x-scope": [
                        ""
                    ]
                }
            ],
            "put": {
                "consumes": [
                    "application/json"
                ],
                "operationId": "organisation_update",
                "parameters": [
                    {
                        "in": "body",
                        "name": "data",
                        "schema": {
                            "$ref": "#/definitions/organisation_update",
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
                            "$ref": "#/definitions/organisation",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:organisation:update"
                ]
            }
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
                        "collectionFormat": "csv",
                        "description": "An optional list of permission ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:permission:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:permission:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:permission:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:permission:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:permission:update"
                ]
            }
        },
        "/refresh/all": {
            "get": {
                "description": "Refresh all mapping information",
                "operationId": "refresh_all",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed all mapping data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/clients": {
            "get": {
                "description": "Refresh OIDC client information",
                "operationId": "refresh_clients",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed OIDC client data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/domains": {
            "get": {
                "description": "Refresh domain mapping information",
                "operationId": "refresh_domains",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed domain mapping data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/keys": {
            "get": {
                "description": "Refresh JWKS information",
                "operationId": "refresh_keys",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed keys data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/permissions": {
            "get": {
                "description": "Refresh permission mapping information",
                "operationId": "refresh_permissions",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed permission mapping data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/resources": {
            "get": {
                "description": "Refresh resource mapping information",
                "operationId": "refresh_resources",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed resource mapping data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/roles": {
            "get": {
                "description": "Refresh role mapping information",
                "operationId": "refresh_roles",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed role mapping data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
        },
        "/refresh/sites": {
            "get": {
                "description": "Refresh site mapping information",
                "operationId": "refresh_sites",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "Successfully refreshed site mapping data"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                }
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
                {
                    "$ref": "#/parameters/optional_nocache",
                    "x-scope": [
                        ""
                    ]
                }
            ]
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
                        "collectionFormat": "csv",
                        "description": "An optional list of resource ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:resource:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:resource:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:resource:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:resource:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:resource:update"
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:roleresourcepermission:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:roleresourcepermission:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:roleresourcepermission:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:roleresourcepermission:update"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                        "collectionFormat": "csv",
                        "description": "An optional list of role ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:role:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:role:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:role:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:role:read"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:role:update"
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
                        "collectionFormat": "csv",
                        "description": "An optional list of site ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:sitedataschema:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:sitedataschema:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:sitedataschema:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:sitedataschema:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:sitedataschema:update"
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:siterole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:siterole:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:siterole:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:siterole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:siterole:update"
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
                        "collectionFormat": "csv",
                        "description": "An optional list of site ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
                        "name": "site_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    },
                    {
                        "description": "An optional client id to filter on",
                        "in": "query",
                        "name": "client_id",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:site:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:site:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:site:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:site:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:site:update"
                ]
            }
        },
        "/sites/{site_id}/activate": {
            "get": {
                "deprecated": true,
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
                    "$ref": "#/parameters/optional_portal_context_header",
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
        "/sites/{site_id}/deactivate": {
            "get": {
                "deprecated": true,
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
                    "$ref": "#/parameters/optional_portal_context_header",
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:userdomainrole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:userdomainrole:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:userdomainrole:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:userdomainrole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                        "description": "An optional birth_date range filter",
                        "in": "query",
                        "name": "birth_date",
                        "required": false,
                        "type": "string",
                        "x-aor-filter": {
                            "format": "date",
                            "range": true
                        }
                    },
                    {
                        "description": "An optional country filter",
                        "in": "query",
                        "maxLength": 2,
                        "minLength": 2,
                        "name": "country",
                        "required": false,
                        "type": "string",
                        "x-related-info": {
                            "label": "name",
                            "rest_resource_name": "countries"
                        }
                    },
                    {
                        "description": "An optional date joined range filter",
                        "in": "query",
                        "name": "date_joined",
                        "required": false,
                        "type": "string",
                        "x-aor-filter": {
                            "format": "date",
                            "range": true
                        }
                    },
                    {
                        "description": "An optional case insensitive email inner match filter",
                        "in": "query",
                        "minLength": 3,
                        "name": "email",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional email verified filter",
                        "in": "query",
                        "name": "email_verified",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "description": "An optional case insensitive first name inner match filter",
                        "in": "query",
                        "minLength": 3,
                        "name": "first_name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional gender filter",
                        "in": "query",
                        "name": "gender",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional is_active filter",
                        "in": "query",
                        "name": "is_active",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "description": "An optional last login range filter",
                        "in": "query",
                        "name": "last_login",
                        "required": false,
                        "type": "string",
                        "x-aor-filter": {
                            "format": "date",
                            "range": true
                        }
                    },
                    {
                        "description": "An optional case insensitive last name inner match filter",
                        "in": "query",
                        "minLength": 3,
                        "name": "last_name",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional case insensitive MSISDN inner match filter",
                        "in": "query",
                        "minLength": 3,
                        "name": "msisdn",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional MSISDN verified filter",
                        "in": "query",
                        "name": "msisdn_verified",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "description": "An optional case insensitive nickname inner match filter",
                        "in": "query",
                        "minLength": 3,
                        "name": "nickname",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional filter on the organisation id",
                        "in": "query",
                        "name": "organisation_id",
                        "required": false,
                        "type": "integer"
                    },
                    {
                        "description": "An optional updated_at range filter",
                        "in": "query",
                        "name": "updated_at",
                        "required": false,
                        "type": "string",
                        "x-aor-filter": {
                            "format": "date-time",
                            "range": true
                        }
                    },
                    {
                        "description": "An optional case insensitive username inner match filter",
                        "in": "query",
                        "minLength": 3,
                        "name": "username",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional case insensitive inner match filter across all searchable text fields",
                        "in": "query",
                        "minLength": 3,
                        "name": "q",
                        "required": false,
                        "type": "string"
                    },
                    {
                        "description": "An optional filter based on whether a user has 2FA enabled or not",
                        "in": "query",
                        "name": "tfa_enabled",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "description": "An optional filter based on whether a user belongs to an organisation or not",
                        "in": "query",
                        "name": "has_organisation",
                        "required": false,
                        "type": "boolean"
                    },
                    {
                        "collectionFormat": "csv",
                        "description": "Fields and directions to order by, e.g. \\"-created_at,username\\". Add \\"-\\" in front of a field name to indicate descending order.",
                        "in": "query",
                        "items": {
                            "type": "string"
                        },
                        "name": "order_by",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    },
                    {
                        "collectionFormat": "csv",
                        "description": "An optional list of user ids",
                        "in": "query",
                        "items": {
                            "format": "uuid",
                            "type": "string"
                        },
                        "minItems": 1,
                        "name": "user_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true
                    },
                    {
                        "collectionFormat": "csv",
                        "description": "An optional list of site ids",
                        "in": "query",
                        "items": {
                            "type": "integer"
                        },
                        "minItems": 1,
                        "name": "site_ids",
                        "required": false,
                        "type": "array",
                        "uniqueItems": true,
                        "x-related-info": {
                            "label": "name",
                            "rest_resource_name": "sites"
                        }
                    }
                ],
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:user:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ]
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
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:user:delete"
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
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:user:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                            "$ref": "#/definitions/user_update",
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
                            "$ref": "#/definitions/user",
                            "x-scope": [
                                ""
                            ]
                        }
                    }
                },
                "tags": [
                    "authentication"
                ],
                "x-aor-permissions": [
                    "urn:ge:identity_provider:user:update"
                ]
            }
        },
        "/users/{user_id}/activate": {
            "get": {
                "deprecated": true,
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                "deprecated": true,
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
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:usersitedata:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:usersitedata:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:usersitedata:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:usersitedata:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:user_data:usersitedata:update"
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
                        "headers": {
                            "X-Total-Count": {
                                "description": "The total number of results matching the query",
                                "type": "integer"
                            }
                        },
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:usersiterole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                }
            ],
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:usersiterole:create"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:usersiterole:delete"
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
                ],
                "x-aor-permissions": [
                    "urn:ge:access_control:usersiterole:read"
                ]
            },
            "parameters": [
                {
                    "$ref": "#/parameters/optional_portal_context_header",
                    "x-scope": [
                        ""
                    ]
                },
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
    "swagger": "2.0",
    "x-detail-page-definitions": {
        "domain": {
            "inlines": [
                {
                    "fields": [
                        "id",
                        "name",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "parent_id",
                    "label": "Child Domains",
                    "model": "domain"
                },
                {
                    "fields": [
                        "role_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "domain_id",
                    "label": "Roles",
                    "model": "domain_role"
                }
            ]
        },
        "invitation": {
            "inlines": [
                {
                    "fields": [
                        "domain_id",
                        "role_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "invitation_id",
                    "label": "Domain Roles",
                    "model": "invitation_domain_role"
                },
                {
                    "fields": [
                        "site_id",
                        "role_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "invitation_id",
                    "label": "Site Roles",
                    "model": "invitation_site_role"
                }
            ]
        },
        "role": {
            "inlines": [
                {
                    "fields": [
                        "resource_id",
                        "permission_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "role_id",
                    "label": "Resource Permissions",
                    "model": "role_resource_permission"
                }
            ]
        },
        "site": {
            "inlines": [
                {
                    "fields": [
                        "role_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "site_id",
                    "label": "Roles",
                    "model": "site_role"
                }
            ]
        },
        "user": {
            "inlines": [
                {
                    "fields": [
                        "domain_id",
                        "role_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "user_id",
                    "label": "Domain Roles",
                    "model": "user_domain_role"
                },
                {
                    "fields": [
                        "site_id",
                        "data",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "user_id",
                    "label": "Site Data",
                    "model": "user_site_data",
                    "rest_resource_name": "usersitedata"
                },
                {
                    "fields": [
                        "site_id",
                        "role_id",
                        "created_at",
                        "updated_at"
                    ],
                    "key": "user_id",
                    "label": "Site Roles",
                    "model": "user_site_role"
                }
            ]
        }
    }
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
