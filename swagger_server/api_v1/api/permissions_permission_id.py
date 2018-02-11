# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class PermissionsPermissionId(ApiHandler):

    def get(self, permission_id):

        return {'created_at': 'something', 'updated_at': 'something', 'id': 9573, 'name': 'something'}, 200, None

    def put(self, permission_id):
        print(self.json)

        return {'created_at': 'something', 'updated_at': 'something', 'id': 9573, 'name': 'something'}, 200, None

    def delete(self, permission_id):

        return None, 204, None