# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class OpsAllUserRolesUserId(ApiHandler):

    def get(self, user_id):

        return {'roles_map': {}, 'user_id': 'something'}, 200, None