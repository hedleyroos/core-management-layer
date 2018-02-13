# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class InvitationdomainrolesInvitationIdDomainIdRoleId(ApiHandler):

    def get(self, invitation_id, domain_id, role_id):

        return {'role_id': 9573, 'created_at': 'something', 'invitation_id': 'something', 'updated_at': 'something', 'domain_id': 9573}, 200, None

    def delete(self, invitation_id, domain_id, role_id):

        return None, 204, None