# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class OpsUserSiteRoleLabelsAggregatedUserIdSiteId(ApiHandler):

    def get(self, user_id, site_id):

        return {}, 200, None