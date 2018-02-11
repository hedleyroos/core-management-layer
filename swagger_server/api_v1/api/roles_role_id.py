# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class RolesRoleId(ApiHandler):

    def get(self, role_id):

        return {'created_at': 'something', 'label': {}, 'requires_2fa': False, 'id': 9573, 'updated_at': 'something'}, 200, None

    def put(self, role_id):
        print(self.json)

        return {'created_at': 'something', 'label': {}, 'requires_2fa': False, 'id': 9573, 'updated_at': 'something'}, 200, None

    def delete(self, role_id):

        return None, 204, None