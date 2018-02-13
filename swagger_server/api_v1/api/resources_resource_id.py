# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ResourcesResourceId(ApiHandler):

    def get(self, resource_id):

        return {'created_at': 'something', 'id': 9573, 'urn': 'something', 'updated_at': 'something'}, 200, None

    def put(self, resource_id):
        print(self.json)

        return {'created_at': 'something', 'id': 9573, 'urn': 'something', 'updated_at': 'something'}, 200, None

    def delete(self, resource_id):

        return None, 204, None