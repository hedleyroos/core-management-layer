# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class UsersitedataUserIdSiteId(ApiHandler):

    def get(self, user_id, site_id):

        return {'blocked': False, 'site_id': 9573, 'user_id': 'something', 'created_at': 'something', 'data': {}, 'updated_at': 'something', 'consented_at': 'something'}, 200, None

    def put(self, user_id, site_id):
        print(self.json)

        return {'blocked': False, 'site_id': 9573, 'user_id': 'something', 'created_at': 'something', 'data': {}, 'updated_at': 'something', 'consented_at': 'something'}, 200, None

    def delete(self, user_id, site_id):

        return None, 204, None