#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'The Management Layer API exposes the functionality that is available to users. Access to this API is based on a user token that must be presented with every request.  The Management Layer ties together the User Data Store, Access Control System and Authentication Service. It performs permission checking and audit logging. '})
    app.run(port=8080)
