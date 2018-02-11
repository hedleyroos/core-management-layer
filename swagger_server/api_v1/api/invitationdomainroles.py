# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Invitationdomainroles(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'role_id': 9573, 'created_at': 'something', 'invitation_id': 'something', 'updated_at': 'something', 'domain_id': 9573}, 201, None