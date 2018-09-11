Changelog
=========

1.8.0
-----
* Added `POST /ops/usersitedata` API call in case a site needs to create a UserSiteData entry.
* The `DELETE /users/{user_id}` and `GET /request_user_deletion` API calls not return an HTTP 400
  if the user making the request is also the user to be deleted.

1.7.0
-----
Added `GET /ops/usersitedata` and `PUT /ops/usersitedata` API calls.

1.6.0
-----
Prometheus instrumentation added

1.5.0
-----
Replaced Memcache with Redis

1.4.2
-----
Added checks to ensure that only a user that has certain roles can assign/delete those roles
when creating or editing invitations.

1.4.1
-----
Bugfix for Admin notes
Made changes to the adminnote paths based on current UDS definition.
Removed creator_id from adminnote_create object and marked as not required.
Fixed get_users_with_roles_for_domain test
Added fix for sentry bug of missing user_id. Also added continuous call to get all resources if more than limit.
Moved initialisation of ClientSession into an async function to get rid of the warning
Added purge invite endpoint
Added invitation CRUD endpoints
Added Organisation Create/Delete/Update Endpoints on Management layer, regenerated, and updated tests.
Updated Authentication Service swagger and client regenerated.
Allow Management Portal to call the get_sites_under_domain API call
Added extra check to verify that a user is associated with an organisation before assigning a role on a site or domain.
Added flag to allow specifying API calls which are allowed to be made by the Management Portal
Read and list operations for domains and sites no longer requires any permissions

1.4.0
-----
Added API calls for invitation system

1.3.0
-----
Re-worked to use openapi-generator: https://github.com/OpenAPITools/openapi-generator (a fork of swagger-generator).

1.2.0
-----
Addition of healtcheck API end-point

1.1.0
-----
Addition of the `/ops/get_sites_under_domain/{domain_id}` API end-point.

1.0.0
-----
Initial release
