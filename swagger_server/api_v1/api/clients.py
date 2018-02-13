# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Clients(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None