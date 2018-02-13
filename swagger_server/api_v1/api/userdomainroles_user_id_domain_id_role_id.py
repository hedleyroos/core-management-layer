# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class UserdomainrolesUserIdDomainIdRoleId(ApiHandler):

    def get(self, user_id, domain_id, role_id):

        return {'role_id': 9573, 'user_id': 'something', 'updated_at': 'something', 'created_at': 'something', 'domain_id': 9573}, 200, None

    def delete(self, user_id, domain_id, role_id):

        return None, 204, None