# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class InvitationsInvitationId(ApiHandler):

    def get(self, invitation_id):

        return {'invitor_id': 'something', 'id': 'something', 'updated_at': 'something', 'created_at': 'something', 'first_name': 'something', 'expires_at': 'something', 'last_name': 'something', 'email': 'something'}, 200, None

    def put(self, invitation_id):
        print(self.json)

        return {'invitor_id': 'something', 'id': 'something', 'updated_at': 'something', 'created_at': 'something', 'first_name': 'something', 'expires_at': 'something', 'last_name': 'something', 'email': 'something'}, 200, None

    def delete(self, invitation_id):

        return None, 204, None