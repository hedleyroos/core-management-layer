# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Siteroles(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'role_id': 9573, 'created_at': 'something', 'grant_implicitly': False, 'site_id': 9573, 'updated_at': 'something'}, 201, None