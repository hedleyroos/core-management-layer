import json

from aiohttp import web


class JSONException(web.HTTPException):
    status_code = None

    def __init__(self, *, headers=None, reason=None, body=None,
                 text=None, message=None):
        text = json.dumps(text) if text else json.dumps({"message": message})
        super().__init__(headers=headers, reason=reason, body=body,
                         text=text, content_type="application/json")


class JSONBadRequest(JSONException):
    status_code = 400


class JSONUnauthorized(JSONException):
    status_code = 401


class JSONForbidden(JSONException):
    status_code = 403


class JSONNotFound(JSONException):
    status_code = 404


class JSONBadGateway(JSONException):
    status_code = 502
