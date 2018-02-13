# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Sitedataschemas(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'created_at': 'something', 'schema': {}, 'site_id': 9573, 'updated_at': 'something'}, 201, None