# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Invitations(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'invitor_id': 'something', 'id': 'something', 'updated_at': 'something', 'created_at': 'something', 'first_name': 'something', 'expires_at': 'something', 'last_name': 'something', 'email': 'something'}, 201, None