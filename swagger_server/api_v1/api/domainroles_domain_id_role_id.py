# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class DomainrolesDomainIdRoleId(ApiHandler):

    def get(self, domain_id, role_id):

        return {'role_id': 9573, 'created_at': 'something', 'updated_at': 'something', 'grant_implicitly': False, 'domain_id': 9573}, 200, None

    def put(self, domain_id, role_id):
        print(self.json)

        return {'role_id': 9573, 'created_at': 'something', 'updated_at': 'something', 'grant_implicitly': False, 'domain_id': 9573}, 200, None

    def delete(self, domain_id, role_id):

        return None, 204, None