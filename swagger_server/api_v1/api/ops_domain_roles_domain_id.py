# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class OpsDomainRolesDomainId(ApiHandler):

    def get(self, domain_id):

        return {'roles_map': {}, 'domain_id': 9573}, 200, None