# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class SitesSiteIdDeactivate(ApiHandler):

    def get(self, site_id):

        return None, 200, None