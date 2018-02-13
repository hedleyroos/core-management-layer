# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Roleresourcepermissions(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'role_id': 9573, 'permission_id': 9573, 'resource_id': 9573, 'updated_at': 'something', 'created_at': 'something'}, 201, None