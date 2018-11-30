import json

from aiohttp import web


class JSONException(web.HTTPException):
    status_code = None

    def __init__(self, *, headers=None, reason=None, body=None,
                 json_data=None, message=None):
        # Use the json object given or create a message object using the string in message.
        text = json.dumps(json_data) if json_data else json.dumps({"message": message})
        # Super the web HTTPException, however force the content_type to application/json.
        super().__init__(headers=headers, reason=reason, body=body, text=text,
                         content_type="application/json")


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
