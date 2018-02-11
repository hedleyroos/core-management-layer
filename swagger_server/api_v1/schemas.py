# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/api/v1'


DefinitionsDomain = {'type': 'object', 'properties': {'id': {'type': 'integer', 'readOnly': True}, 'parent_id': {'type': 'integer'}, 'name': {'type': 'string', 'maxLength': 100}, 'description': {'type': 'string'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'name', 'created_at', 'updated_at']}
DefinitionsRole_label = {'type': 'string', 'maxLength': 100}
DefinitionsSite_role = {'type': 'object', 'properties': {'site_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'grant_implicitly': {'type': 'boolean'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['site_id', 'role_id', 'grant_implicitly', 'created_at', 'updated_at']}
DefinitionsDomain_role_create = {'type': 'object', 'properties': {'domain_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'grant_implicitly': {'type': 'boolean'}}, 'required': ['domain_id', 'role_id']}
DefinitionsInvitation_update = {'type': 'object', 'properties': {'first_name': {'type': 'string', 'maxLength': 100}, 'last_name': {'type': 'string', 'maxLength': 100}, 'email': {'type': 'string', 'format': 'email'}, 'expires_at': {'type': 'string', 'format': 'date-time'}}, 'minProperties': 1}
DefinitionsAdmin_note_create = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'creator_id': {'type': 'string', 'format': 'uuid', 'readOnly': True, 'description': 'The user making the request will be considered the creator and thus this field is not available when creating admin note.'}, 'note': {'type': 'string'}}, 'required': ['user_id', 'creator_id', 'note']}
DefinitionsPermission_update = {'type': 'object', 'properties': {'name': {'type': 'string', 'maxLength': 50}, 'description': {'type': 'string'}}, 'minProperties': 1}
DefinitionsAddress = {'description': 'OIDC Address structure', 'properties': {'street_address': {'type': 'string'}, 'locality': {'type': 'string'}, 'region': {'type': 'string'}, 'postal_code': {'type': 'string'}, 'country': {'type': 'string'}}}
DefinitionsClient = {'description': 'Client object', 'required': ['client_name', 'client_uri'], 'properties': {'client_id': {'type': 'string'}, 'redirect_uris': {'type': 'array', 'items': {'type': 'string'}}, 'response_types': {'type': 'array', 'items': {'type': 'string'}}, 'grant_types': {'type': 'array', 'items': {'type': 'string'}}, 'application_type': {'type': 'string'}, 'contacts': {'type': 'array', 'items': {'type': 'string'}}, 'client_name': {'type': 'string'}, 'logo_uri': {'type': 'string'}, 'client_uri': {'type': 'string'}, 'policy_uri': {'type': 'string'}, 'tos_uri': {'type': 'string'}, 'default_max_age': {'type': 'integer', 'format': 'int64'}, 'default_scopes': {'type': 'array', 'items': {'type': 'string'}}}, 'minProperties': 1}
DefinitionsAdmin_note_update = {'type': 'object', 'properties': {'note': {'type': 'string'}}, 'minProperties': 1}
DefinitionsUser_site_data_create = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'consented_at': {'type': 'string', 'format': 'date'}, 'blocked': {'type': 'boolean'}, 'data': {'type': 'object'}}, 'required': ['user_id', 'site_id', 'data']}
DefinitionsSite_update = {'type': 'object', 'properties': {'client_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'name': {'type': 'string', 'maxLength': 100}, 'description': {'type': 'string'}, 'is_active': {'type': 'boolean'}}, 'minProperties': 1}
DefinitionsSite_data_schema_create = {'type': 'object', 'properties': {'site_id': {'type': 'integer'}, 'schema': {'type': 'object'}}, 'required': ['site_id', 'schema']}
DefinitionsUser_site_data_update = {'type': 'object', 'properties': {'consented_at': {'type': 'string', 'format': 'date'}, 'blocked': {'type': 'boolean'}, 'data': {'type': 'object'}}, 'minProperties': 1}
DefinitionsRole_resource_permission_create = {'type': 'object', 'properties': {'role_id': {'type': 'integer'}, 'resource_id': {'type': 'integer'}, 'permission_id': {'type': 'integer'}}, 'required': ['role_id', 'resource_id', 'permission_id']}
DefinitionsPermission_create = {'type': 'object', 'properties': {'name': {'type': 'string', 'maxLength': 50}, 'description': {'type': 'string'}}, 'required': ['name']}
DefinitionsInvitation_domain_role_create = {'type': 'object', 'properties': {'invitation_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}}, 'required': ['invitation_id', 'domain_id', 'role_id']}
DefinitionsUser_site_role = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['user_id', 'site_id', 'role_id', 'created_at', 'updated_at']}
DefinitionsResource_create = {'type': 'object', 'properties': {'urn': {'type': 'string', 'format': 'uri'}, 'description': {'type': 'string'}}, 'required': ['urn']}
DefinitionsResource_update = {'type': 'object', 'properties': {'urn': {'type': 'string', 'format': 'uri'}, 'description': {'type': 'string'}}, 'minProperties': 1}
DefinitionsPermission = {'type': 'object', 'properties': {'id': {'type': 'integer', 'readOnly': True}, 'name': {'type': 'string', 'maxLength': 50}, 'description': {'type': 'string'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'name', 'created_at', 'updated_at']}
DefinitionsInvitation = {'type': 'object', 'properties': {'id': {'type': 'string', 'format': 'uuid', 'readOnly': True}, 'invitor_id': {'type': 'string', 'format': 'uuid', 'description': 'The user that created the invitation'}, 'first_name': {'type': 'string', 'maxLength': 100}, 'last_name': {'type': 'string', 'maxLength': 100}, 'email': {'type': 'string', 'format': 'email'}, 'expires_at': {'type': 'string', 'format': 'date-time'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'invitor_id', 'first_name', 'last_name', 'email', 'expires_at', 'created_at', 'updated_at']}
DefinitionsSite = {'type': 'object', 'properties': {'id': {'type': 'integer', 'readOnly': True}, 'client_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'name': {'type': 'string', 'maxLength': 100}, 'description': {'type': 'string'}, 'is_active': {'type': 'boolean'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'domain_id', 'name', 'is_active', 'created_at', 'updated_at']}
DefinitionsDomain_update = {'type': 'object', 'properties': {'parent_id': {'type': 'integer'}, 'name': {'type': 'string', 'maxLength': 100}, 'description': {'type': 'string'}}, 'minProperties': 1}
DefinitionsUser = {'type': 'object', 'properties': {'id': {'description': 'The UUID of the user', 'type': 'string', 'format': 'uuid', 'readOnly': True}, 'username': {'description': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', 'type': 'string', 'readOnly': True}, 'first_name': {'description': '', 'type': 'string'}, 'last_name': {'description': '', 'type': 'string'}, 'email': {'description': '', 'type': 'string', 'format': 'email'}, 'is_active': {'description': 'Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', 'type': 'boolean'}, 'date_joined': {'description': '', 'type': 'string', 'format': 'date', 'readOnly': True}, 'last_login': {'description': '', 'type': 'string', 'readOnly': True}, 'email_verified': {'type': 'boolean'}, 'msisdn_verified': {'type': 'boolean'}, 'msisdn': {'type': 'string', 'maxLength': 15}, 'gender': {'type': 'string'}, 'birth_date': {'type': 'string', 'format': 'date'}, 'avatar': {'type': 'string', 'format': 'uri'}, 'country_code': {'type': 'string', 'maxLength': 2}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'username', 'is_active', 'date_joined', 'created_at', 'updated_at']}
DefinitionsSite_create = {'type': 'object', 'properties': {'client_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'name': {'type': 'string', 'maxLength': 100}, 'is_active': {'type': 'boolean'}, 'description': {'type': 'string'}}, 'required': ['domain_id', 'name']}
DefinitionsSite_data_schema = {'type': 'object', 'properties': {'site_id': {'type': 'integer'}, 'schema': {'type': 'object'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['site_id', 'schema', 'created_at', 'updated_at']}
DefinitionsUser_domain_role_create = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}}, 'required': ['user_id', 'domain_id', 'role_id']}
DefinitionsResource = {'type': 'object', 'properties': {'id': {'type': 'integer', 'readOnly': True}, 'urn': {'type': 'string', 'format': 'uri'}, 'description': {'type': 'string'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'urn', 'created_at', 'updated_at']}
DefinitionsUser_update = {'type': 'object', 'properties': {'first_name': {'description': '', 'type': 'string'}, 'last_name': {'description': '', 'type': 'string'}, 'email': {'description': '', 'type': 'string', 'format': 'email'}, 'is_active': {'description': 'Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', 'type': 'boolean'}, 'email_verified': {'type': 'boolean'}, 'msisdn_verified': {'type': 'boolean'}, 'msisdn': {'type': 'string', 'maxLength': 15}, 'gender': {'type': 'string'}, 'birth_date': {'type': 'string', 'format': 'date'}, 'avatar': {'type': 'string', 'format': 'uri'}, 'country_code': {'type': 'string', 'maxLength': 2}}, 'minProperties': 1}
DefinitionsDomain_role_update = {'type': 'object', 'properties': {'grant_implicitly': {'type': 'boolean'}}, 'minProperties': 1}
DefinitionsRole_resource_permission = {'type': 'object', 'properties': {'role_id': {'type': 'integer'}, 'resource_id': {'type': 'integer'}, 'permission_id': {'type': 'integer'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['role_id', 'resource_id', 'permission_id', 'created_at', 'updated_at']}
DefinitionsAdmin_note = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'creator_id': {'type': 'string', 'format': 'uuid', 'readOnly': True, 'description': 'The user making the request will be considered the creator and thus this field is not available when creating admin note.'}, 'note': {'type': 'string'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['user_id', 'creator_id', 'note', 'created_at', 'updated_at']}
DefinitionsSite_role_update = {'type': 'object', 'properties': {'grant_implicitly': {'type': 'boolean'}}, 'minProperties': 1}
DefinitionsUser_site_role_create = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}}, 'required': ['user_id', 'site_id', 'role_id']}
DefinitionsUser_domain_role = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['user_id', 'domain_id', 'role_id', 'created_at', 'updated_at']}
DefinitionsSite_role_create = {'type': 'object', 'properties': {'site_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'grant_implicitly': {'type': 'boolean'}}, 'required': ['site_id', 'role_id']}
DefinitionsSite_and_domain_roles = {'description': 'An object containing the site- and domain lineage roles defined for a given site.', 'type': 'object', 'properties': {'site_id': {'description': 'The site for which the request was made.', 'type': 'integer'}, 'roles_map': {'description': 'A dictionary where the keys are site and domain ids prefixed with `s:` and `d:`, respectively and the values are lists of role ids.', 'additionalProperties': {'description': 'The list of role ids for the site or domain', 'type': 'array', 'items': {'type': 'integer'}}, 'example': {'s:1': [1, 2, 3], 'd:1': [1], 'd:2': [1, 2]}}}, 'required': ['site_id', 'roles_map']}
DefinitionsClient_create = {'type': 'object', 'properties': {'_post_logout_redirect_uris': {'description': 'New-line delimited list of post-logout redirect URIs', 'type': 'string'}, '_redirect_uris': {'description': 'New-line delimited list of redirect URIs', 'type': 'string'}, 'client_id': {'description': '', 'type': 'string'}, 'client_type': {'description': '<b>Confidential</b> clients are capable of maintaining the confidentiality of their credentials. <b>Public</b> clients are incapable.', 'type': 'string'}, 'contact_email': {'description': '', 'type': 'string'}, 'jwt_alg': {'description': 'Algorithm used to encode ID Tokens.', 'type': 'string'}, 'logo': {'description': '', 'type': 'string', 'format': 'uri'}, 'name': {'description': '', 'type': 'string'}, 'require_consent': {'description': 'If disabled, the Server will NEVER ask the user for consent.', 'type': 'boolean'}, 'response_type': {'description': '', 'type': 'string'}, 'reuse_consent': {'description': "If enabled, the Server will save the user consent given to a specific client, so that user won't be prompted for the same authorization multiple times.", 'type': 'boolean'}, 'terms_url': {'description': 'External reference to the privacy policy of the client.', 'type': 'string'}, 'website_url': {'description': '', 'type': 'string'}}, 'required': ['client_id', 'response_type']}
DefinitionsInvitation_domain_role = {'type': 'object', 'properties': {'invitation_id': {'type': 'string', 'format': 'uuid'}, 'domain_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['invitation_id', 'domain_id', 'role_id', 'created_at', 'updated_at']}
DefinitionsUser_site_data = {'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'consented_at': {'type': 'string', 'format': 'date'}, 'data': {'type': 'object'}, 'blocked': {'type': 'boolean'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['user_id', 'site_id', 'consented_at', 'blocked', 'data', 'created_at', 'updated_at']}
DefinitionsDomain_roles = {'description': "An object containing the domain roles defined for a given domain and it's lineage.", 'type': 'object', 'properties': {'domain_id': {'description': 'The domain for which the request was made.', 'type': 'integer'}, 'roles_map': {'description': 'A dictionary where the keys are domain ids prefixed with `d:` and the values are lists of role ids.', 'type': 'object', 'additionalProperties': {'description': 'The list of role ids for the domain', 'type': 'array', 'items': {'type': 'integer'}}, 'example': {'s:1': [1, 2, 3], 'd:1': [1], 'd:2': [1, 2]}}}, 'required': ['domain_id', 'roles_map']}
DefinitionsInvitation_site_role = {'type': 'object', 'properties': {'invitation_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['invitation_id', 'site_id', 'role_id', 'created_at', 'updated_at']}
DefinitionsSite_data_schema_update = {'type': 'object', 'properties': {'schema': {'type': 'object'}}, 'minProperties': 1}
DefinitionsInvitation_create = {'type': 'object', 'properties': {'invitor_id': {'type': 'string', 'format': 'uuid', 'description': 'The user that created the invitation'}, 'first_name': {'type': 'string', 'maxLength': 100}, 'last_name': {'type': 'string', 'maxLength': 100}, 'email': {'type': 'string', 'format': 'email'}, 'expires_at': {'type': 'string', 'format': 'date-time'}}, 'required': ['invitor_id', 'first_name', 'last_name', 'email']}
DefinitionsAll_user_roles = {'description': 'An object containing the effective roles that a user has in any place in the organisational tree.', 'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'roles_map': {'type': 'object', 'description': 'Domain and site roles', 'additionalProperties': {'type': 'array', 'items': {'type': 'integer'}}, 'example': {'s:1': [1, 2, 3], 'd:1': [1], 'd:2': [1, 2]}}}, 'required': ['user_id', 'roles_map']}
DefinitionsInvitation_site_role_create = {'type': 'object', 'properties': {'invitation_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}}, 'required': ['invitation_id', 'site_id', 'role_id']}
DefinitionsDomain_role = {'type': 'object', 'properties': {'domain_id': {'type': 'integer'}, 'role_id': {'type': 'integer'}, 'grant_implicitly': {'type': 'boolean'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['domain_id', 'role_id', 'grant_implicitly', 'created_at', 'updated_at']}
DefinitionsDomain_create = {'type': 'object', 'properties': {'parent_id': {'type': 'integer'}, 'name': {'type': 'string', 'maxLength': 100}, 'description': {'type': 'string'}}, 'required': ['name']}
DefinitionsRole_update = {'type': 'object', 'properties': {'label': {'type': 'string', 'maxLength': 100}, 'requires_2fa': {'type': 'boolean'}, 'description': {'type': 'string'}}, 'minProperties': 1}
DefinitionsRole_create = {'type': 'object', 'properties': {'label': DefinitionsRole_label, 'requires_2fa': {'type': 'boolean'}, 'description': {'type': 'string'}}, 'required': ['label', 'requires_2fa']}
DefinitionsRole = {'type': 'object', 'properties': {'id': {'type': 'integer', 'readOnly': True}, 'label': DefinitionsRole_label, 'requires_2fa': {'type': 'boolean'}, 'description': {'type': 'string'}, 'created_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}, 'updated_at': {'type': 'string', 'format': 'date-time', 'readOnly': True}}, 'required': ['id', 'label', 'requires_2fa', 'created_at', 'updated_at']}
DefinitionsSite_role_labels_aggregated = {'description': 'An object containing a site ID and an aggregated list of all the role labels supported by the site and all the domains in its lineage.', 'type': 'object', 'properties': {'site_id': {'type': 'integer'}, 'roles': {'type': 'array', 'items': DefinitionsRole_label}}}
DefinitionsUser_site_role_labels_aggregated = {'description': 'An object containing a user ID, site ID and an aggregated list of all the role labels assigned to the user for the site and all the domains in its lineage.', 'type': 'object', 'properties': {'user_id': {'type': 'string', 'format': 'uuid'}, 'site_id': {'type': 'integer'}, 'roles': {'type': 'array', 'items': DefinitionsRole_label}}}
DefinitionsUserinfo = {'description': 'OIDC UserInfo structure', 'required': ['sub'], 'properties': {'sub': {'type': 'string'}, 'name': {'type': 'string'}, 'given_name': {'type': 'string'}, 'family_name': {'type': 'string'}, 'email': {'type': 'string'}, 'email_verified': {'type': 'boolean'}, 'phone_number': {'type': 'string'}, 'phone_number_verified': {'type': 'boolean'}, 'address': DefinitionsAddress}}

validators = {
    ('domains', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'domain_ids': {'description': 'An optional list of domain ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('domains', 'POST'): {'json': DefinitionsDomain_create},
    ('domains_domain_id', 'PUT'): {'json': DefinitionsDomain_update},
    ('domainroles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'domain_id': {'description': 'An optional query parameter to filter by domain_id', 'required': False, 'type': 'integer'}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}}}},
    ('domainroles', 'POST'): {'json': DefinitionsDomain_role_create},
    ('domainroles_domain_id_role_id', 'PUT'): {'json': DefinitionsDomain_role_update},
    ('invitations', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'invitor_id': {'description': 'Optional filter based on the invitor (the user who created the invitation)', 'required': False, 'type': 'string', 'format': 'uuid'}, 'invitation_ids': {'description': 'An optional list of invitation ids', 'type': 'array', 'items': {'type': 'integer', 'format': 'uuid'}, 'required': False}}}},
    ('invitations', 'POST'): {'json': DefinitionsInvitation_create},
    ('invitations_invitation_id', 'PUT'): {'json': DefinitionsInvitation_update},
    ('invitationdomainroles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'invitation_id': {'description': 'An optional query parameter to filter by invitation_id', 'required': False, 'type': 'string', 'format': 'uuid'}, 'domain_id': {'description': 'An optional query parameter to filter by domain_id', 'required': False, 'type': 'integer'}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}}}},
    ('invitationdomainroles', 'POST'): {'json': DefinitionsInvitation_domain_role_create},
    ('invitationsiteroles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'invitation_id': {'description': 'An optional query parameter to filter by invitation_id', 'required': False, 'type': 'string', 'format': 'uuid'}, 'site_id': {'description': 'An optional query parameter to filter by site_id', 'required': False, 'type': 'integer'}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}}}},
    ('invitationsiteroles', 'POST'): {'json': DefinitionsInvitation_site_role_create},
    ('permissions', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'permission_ids': {'description': 'An optional list of permission ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('permissions', 'POST'): {'json': DefinitionsPermission_create},
    ('permissions_permission_id', 'PUT'): {'json': DefinitionsPermission_update},
    ('resources', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'prefix': {'description': 'An optional URN prefix filter', 'required': False, 'type': 'string'}, 'resource_ids': {'description': 'An optional list of resource ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('resources', 'POST'): {'json': DefinitionsResource_create},
    ('resources_resource_id', 'PUT'): {'json': DefinitionsResource_update},
    ('roles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'role_ids': {'description': 'An optional list of role ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('roles', 'POST'): {'json': DefinitionsRole_create},
    ('roles_role_id', 'PUT'): {'json': DefinitionsRole_update},
    ('roleresourcepermissions', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}, 'resource_id': {'description': 'An optional resource filter', 'required': False, 'type': 'integer'}, 'permission_id': {'description': 'An optional permission filter', 'required': False, 'type': 'integer'}}}},
    ('roleresourcepermissions', 'POST'): {'json': DefinitionsRole_resource_permission_create},
    ('sites', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'site_ids': {'description': 'An optional list of site ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('sites', 'POST'): {'json': DefinitionsSite_create},
    ('sites_site_id', 'PUT'): {'json': DefinitionsSite_update},
    ('siteroles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'site_id': {'description': 'An optional query parameter to filter by site_id', 'required': False, 'type': 'integer'}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}}}},
    ('siteroles', 'POST'): {'json': DefinitionsSite_role_create},
    ('siteroles_site_id_role_id', 'PUT'): {'json': DefinitionsSite_role_update},
    ('userdomainroles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'user_id': {'description': 'An optional query parameter to filter by user_id', 'required': False, 'type': 'string', 'format': 'uuid'}, 'domain_id': {'description': 'An optional query parameter to filter by domain_id', 'required': False, 'type': 'integer'}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}}}},
    ('userdomainroles', 'POST'): {'json': DefinitionsUser_domain_role_create},
    ('usersiteroles', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'user_id': {'description': 'An optional query parameter to filter by user_id', 'required': False, 'type': 'string', 'format': 'uuid'}, 'site_id': {'description': 'An optional query parameter to filter by site_id', 'required': False, 'type': 'integer'}, 'role_id': {'description': 'An optional query parameter to filter by role_id', 'required': False, 'type': 'integer'}}}},
    ('usersiteroles', 'POST'): {'json': DefinitionsUser_site_role_create},
    ('usersitedata', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'user_id': {'description': 'An optional query parameter to filter by user_id', 'required': False, 'type': 'string', 'format': 'uuid'}, 'site_id': {'description': 'An optional query parameter to filter by site_id', 'required': False, 'type': 'integer'}}}},
    ('usersitedata', 'POST'): {'json': DefinitionsUser_site_data_create},
    ('usersitedata_user_id_site_id', 'PUT'): {'json': DefinitionsUser_site_data_update},
    ('adminnotes', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'user_id': {'description': 'An optional query parameter to filter by user_id', 'required': False, 'type': 'string', 'format': 'uuid'}, 'creator_id': {'description': 'An optional query parameter to filter by creator (a user_id)', 'required': False, 'type': 'string', 'format': 'uuid'}}}},
    ('adminnotes', 'POST'): {'json': DefinitionsAdmin_note_create},
    ('adminnotes_user_id_creator_id_created_at', 'PUT'): {'json': DefinitionsAdmin_note_update},
    ('sitedataschemas', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'site_ids': {'description': 'An optional list of site ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('sitedataschemas', 'POST'): {'json': DefinitionsSite_data_schema_create},
    ('sitedataschemas_site_id', 'PUT'): {'json': DefinitionsSite_data_schema_update},
    ('clients', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'client_ids': {'description': 'An optional list of client ids', 'type': 'array', 'items': {'type': 'integer'}, 'required': False}}}},
    ('users', 'GET'): {'args': {'required': [], 'properties': {'offset': {'description': 'An optional query parameter specifying the offset in the result set to start from.', 'required': False, 'type': 'integer', 'default': 0, 'minimum': 0}, 'limit': {'description': 'An optional query parameter to limit the number of results returned.', 'required': False, 'type': 'integer', 'minimum': 1, 'maximum': 100, 'default': 20}, 'email': {'description': 'An optional email filter', 'required': False, 'type': 'string', 'format': 'email'}, 'user_ids': {'description': 'An optional list of user ids', 'type': 'array', 'items': {'type': 'string', 'format': 'uuid'}, 'required': False}}}},
    ('users_user_id', 'PUT'): {'json': DefinitionsUser},
}

filters = {
    ('ops_site_role_labels_aggregated_site_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsSite_role_labels_aggregated}, 403: {'headers': None, 'schema': None}},
    ('ops_user_site_role_labels_aggregated_user_id_site_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsUser_site_role_labels_aggregated}, 403: {'headers': None, 'schema': None}},
    ('ops_domain_roles_domain_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsDomain_roles}, 403: {'headers': None, 'schema': None}},
    ('ops_site_and_domain_roles_site_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsSite_and_domain_roles}, 403: {'headers': None, 'schema': None}},
    ('ops_all_user_roles_user_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsAll_user_roles}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('domains', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsDomain}}},
    ('domains', 'POST'): {201: {'headers': None, 'schema': DefinitionsDomain}},
    ('domains_domain_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('domains_domain_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsDomain}},
    ('domains_domain_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsDomain}},
    ('domainroles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsDomain_role}}},
    ('domainroles', 'POST'): {201: {'headers': None, 'schema': DefinitionsDomain_role}},
    ('domainroles_domain_id_role_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('domainroles_domain_id_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsDomain_role}},
    ('domainroles_domain_id_role_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsDomain_role}},
    ('invitations', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsInvitation}}},
    ('invitations', 'POST'): {201: {'headers': None, 'schema': DefinitionsInvitation}},
    ('invitations_invitation_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('invitations_invitation_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsInvitation}},
    ('invitations_invitation_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsInvitation}},
    ('invitationdomainroles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsInvitation_domain_role}}},
    ('invitationdomainroles', 'POST'): {201: {'headers': None, 'schema': DefinitionsInvitation_domain_role}},
    ('invitationdomainroles_invitation_id_domain_id_role_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('invitationdomainroles_invitation_id_domain_id_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsInvitation_domain_role}},
    ('invitationsiteroles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsInvitation_site_role}}},
    ('invitationsiteroles', 'POST'): {201: {'headers': None, 'schema': DefinitionsInvitation_site_role}},
    ('invitationsiteroles_invitation_id_site_id_role_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('invitationsiteroles_invitation_id_site_id_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsInvitation_site_role}},
    ('permissions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsPermission}}},
    ('permissions', 'POST'): {201: {'headers': None, 'schema': DefinitionsPermission}},
    ('permissions_permission_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('permissions_permission_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsPermission}},
    ('permissions_permission_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsPermission}},
    ('resources', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsResource}}},
    ('resources', 'POST'): {201: {'headers': None, 'schema': DefinitionsResource}},
    ('resources_resource_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('resources_resource_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsResource}},
    ('resources_resource_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsResource}},
    ('roles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsRole}}},
    ('roles', 'POST'): {201: {'headers': None, 'schema': DefinitionsRole}},
    ('roles_role_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('roles_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsRole}},
    ('roles_role_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsRole}},
    ('roleresourcepermissions', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsRole_resource_permission}}},
    ('roleresourcepermissions', 'POST'): {201: {'headers': None, 'schema': DefinitionsRole_resource_permission}},
    ('roleresourcepermissions_role_id_resource_id_permission_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('roleresourcepermissions_role_id_resource_id_permission_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsRole_resource_permission}},
    ('sites', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsSite}}},
    ('sites', 'POST'): {201: {'headers': None, 'schema': DefinitionsSite}},
    ('sites_site_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('sites_site_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsSite}},
    ('sites_site_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsSite}},
    ('siteroles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsSite_role}}},
    ('siteroles', 'POST'): {201: {'headers': None, 'schema': DefinitionsSite_role}},
    ('siteroles_site_id_role_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('siteroles_site_id_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsSite_role}},
    ('siteroles_site_id_role_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsSite_role}},
    ('userdomainroles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsUser_domain_role}}},
    ('userdomainroles', 'POST'): {201: {'headers': None, 'schema': DefinitionsUser_domain_role}},
    ('userdomainroles_user_id_domain_id_role_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('userdomainroles_user_id_domain_id_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsUser_domain_role}},
    ('usersiteroles', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsUser_site_role}}},
    ('usersiteroles', 'POST'): {201: {'headers': None, 'schema': DefinitionsUser_site_role}},
    ('usersitedata', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsUser_site_data}}},
    ('usersitedata', 'POST'): {201: {'headers': None, 'schema': DefinitionsUser_site_data}},
    ('usersitedata_user_id_site_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('usersitedata_user_id_site_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsUser_site_data}},
    ('usersitedata_user_id_site_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsUser_site_data}},
    ('adminnotes', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsAdmin_note}}, 403: {'headers': None, 'schema': None}},
    ('adminnotes', 'POST'): {201: {'headers': None, 'schema': DefinitionsAdmin_note}, 403: {'headers': None, 'schema': None}},
    ('adminnotes_user_id_creator_id_created_at', 'DELETE'): {204: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}},
    ('adminnotes_user_id_creator_id_created_at', 'GET'): {200: {'headers': None, 'schema': DefinitionsAdmin_note}, 403: {'headers': None, 'schema': None}},
    ('adminnotes_user_id_creator_id_created_at', 'PUT'): {200: {'headers': None, 'schema': DefinitionsAdmin_note}, 403: {'headers': None, 'schema': None}},
    ('sitedataschemas', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsSite_data_schema}}},
    ('sitedataschemas', 'POST'): {201: {'headers': None, 'schema': DefinitionsSite_data_schema}},
    ('sitedataschemas_site_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('sitedataschemas_site_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsSite_data_schema}},
    ('sitedataschemas_site_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsSite_data_schema}},
    ('clients', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsClient}}},
    ('clients_client_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsClient}},
    ('users', 'GET'): {200: {'headers': None, 'schema': {'type': 'array', 'items': DefinitionsUser}}},
    ('users_user_id', 'DELETE'): {204: {'headers': None, 'schema': None}},
    ('users_user_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsUser}},
    ('users_user_id', 'PUT'): {200: {'headers': None, 'schema': None}},
    ('users_user_id_activate', 'GET'): {200: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('users_user_id_deactivate', 'GET'): {200: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('sites_site_id_activate', 'GET'): {200: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
    ('sites_site_id_deactivate', 'GET'): {200: {'headers': None, 'schema': None}, 403: {'headers': None, 'schema': None}, 404: {'headers': None, 'schema': None}},
}

scopes = {
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):

    import six

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

