# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class SitesSiteId(ApiHandler):

    def get(self, site_id):

        return {'is_active': False, 'name': 'something', 'updated_at': 'something', 'created_at': 'something', 'domain_id': 9573, 'id': 9573}, 200, None

    def put(self, site_id):
        print(self.json)

        return {'is_active': False, 'name': 'something', 'updated_at': 'something', 'created_at': 'something', 'domain_id': 9573, 'id': 9573}, 200, None

    def delete(self, site_id):

        return None, 204, None