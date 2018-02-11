# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class RoleresourcepermissionsRoleIdResourceIdPermissionId(ApiHandler):

    def get(self, role_id, resource_id, permission_id):

        return {'role_id': 9573, 'permission_id': 9573, 'resource_id': 9573, 'updated_at': 'something', 'created_at': 'something'}, 200, None

    def delete(self, role_id, resource_id, permission_id):

        return None, 204, None