# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class SiterolesSiteIdRoleId(ApiHandler):

    def get(self, site_id, role_id):

        return {'role_id': 9573, 'created_at': 'something', 'grant_implicitly': False, 'site_id': 9573, 'updated_at': 'something'}, 200, None

    def put(self, site_id, role_id):
        print(self.json)

        return {'role_id': 9573, 'created_at': 'something', 'grant_implicitly': False, 'site_id': 9573, 'updated_at': 'something'}, 200, None

    def delete(self, site_id, role_id):

        return None, 204, None