"""
Basic example using the Swift service API
https://docs.openstack.org/python-swiftclient/latest/service-api.html

This is different from the lower level connection API providing
more powerful features such as performing multiple operations
asynchronously.

List: https://github.com/openstack/python-swiftclient/blob/89994a7ad02cf11f723a9071a4c96dc757b30583/swiftclient/service.py#L897-L917
"""
import os
import pprint

from swiftclient.service import SwiftService

# NOTE: os_user_domain_name and os_project_domain_name must be present for v3 auth
# We assume here that an rc file is sourced setting these env variables
options = { 
    "auth_version": os.environ["OS_IDENTITY_API_VERSION"],
    "os_username": os.environ["OS_USERNAME"],
    "os_password": os.environ["OS_PASSWORD"],
    "os_user_domain_name": os.environ["OS_USER_DOMAIN_NAME"],
    "os_project_name": os.environ["OS_PROJECT_NAME"],
    "os_project_domain_name": os.environ["OS_PROJECT_DOMAIN_NAME"],
    "os_auth_url": os.environ["OS_AUTH_URL"],
}

with SwiftService(options=options) as swift:
    
    # List your containers
    containers = swift.list()
    print("--- Containers ---")
    pprint.pprint(list(containers))

    # Stats for your account
    print("--- Stats ---")
    pprint.pprint(swift.stat())
