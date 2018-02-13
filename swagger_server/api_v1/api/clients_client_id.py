# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ClientsClientId(ApiHandler):

    def get(self, client_id):

        return {'response_type': 'something', 'id': 9573, 'client_id': 'something'}, 200, None