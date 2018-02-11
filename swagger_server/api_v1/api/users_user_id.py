# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class UsersUserId(ApiHandler):

    def get(self, user_id):

        return {'is_active': False, 'created_at': 'something', 'username': 'something', 'updated_at': 'something', 'date_joined': 'something', 'id': 'something'}, 200, None

    def put(self, user_id):
        print(self.json)

        return None, 200, None

    def delete(self, user_id):

        return None, 204, None