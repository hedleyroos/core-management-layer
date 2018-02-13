# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class AdminnotesUserIdCreatorIdCreatedAt(ApiHandler):

    def get(self, user_id, creator_id, created_at):

        return {'created_at': 'something', 'user_id': 'something', 'note': 'something', 'creator_id': 'something', 'updated_at': 'something'}, 200, None

    def put(self, user_id, creator_id, created_at):
        print(self.json)

        return {'created_at': 'something', 'user_id': 'something', 'note': 'something', 'creator_id': 'something', 'updated_at': 'something'}, 200, None

    def delete(self, user_id, creator_id, created_at):

        return None, 204, None