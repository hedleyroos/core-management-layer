# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Usersitedata(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'blocked': False, 'site_id': 9573, 'user_id': 'something', 'created_at': 'something', 'data': {}, 'updated_at': 'something', 'consented_at': 'something'}, 201, None