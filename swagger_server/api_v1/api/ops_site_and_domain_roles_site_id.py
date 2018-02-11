# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class OpsSiteAndDomainRolesSiteId(ApiHandler):

    def get(self, site_id):

        return {'roles_map': {}, 'site_id': 9573}, 200, None