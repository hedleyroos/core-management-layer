# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class DomainsDomainId(ApiHandler):

    def get(self, domain_id):

        return {'created_at': 'something', 'name': 'something', 'id': 9573, 'updated_at': 'something'}, 200, None

    def put(self, domain_id):
        print(self.json)

        return {'created_at': 'something', 'name': 'something', 'id': 9573, 'updated_at': 'something'}, 200, None

    def delete(self, domain_id):

        return None, 204, None