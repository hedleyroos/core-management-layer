# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Sites(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'is_active': False, 'name': 'something', 'updated_at': 'something', 'created_at': 'something', 'domain_id': 9573, 'id': 9573}, 201, None