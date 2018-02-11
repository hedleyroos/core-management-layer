# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Adminnotes(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'created_at': 'something', 'user_id': 'something', 'note': 'something', 'creator_id': 'something', 'updated_at': 'something'}, 201, None