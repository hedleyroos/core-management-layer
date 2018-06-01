import os
from aiohttp.web_response import json_response

from management_layer import settings
from management_layer.api.views import __SWAGGER_SPEC__


class SwaggerSpec(__SWAGGER_SPEC__):

    async def get(self):
        spec = self.SPEC.copy()
        spec["basePath"] = "/"
        # Removing the host so that the spec the URL is loaded on is used.
        spec.pop("host", None)
        # Add basic auth as a security definition
        security_definitions = spec.get("securityDefinitions", {})
        security_definitions["OAuth2"]["authorizationUrl"] = \
            settings.AUTHENTICATION_SERVICE_API.replace("/api/v1", "/openid/authorize")
        security_definitions["OAuth2"]["tokenUrl"] = \
            settings.AUTHENTICATION_SERVICE_API.replace("/api/v1", "/openid/token")
        spec["securityDefinitions"] = security_definitions
        return json_response(spec)
