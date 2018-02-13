# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class SitedataschemasSiteId(ApiHandler):

    def get(self, site_id):

        return {'created_at': 'something', 'schema': {}, 'site_id': 9573, 'updated_at': 'something'}, 200, None

    def put(self, site_id):
        print(self.json)

        return {'created_at': 'something', 'schema': {}, 'site_id': 9573, 'updated_at': 'something'}, 200, None

    def delete(self, site_id):

        return None, 204, None