"""
Examples using the python keystone client.

We're using sessions to make things a whole lot easier.
"""
import os

from keystoneclient import session
from keystoneclient.auth.identity import v3
from keystoneclient.v3 import client as keystone_client


# Module storage for session
CACHED_SESSION = None

# === Authentication ===

def get_session(output=False):
    """
    Gets a session with your credentials from env vars.
    """
    global CACHED_SESSION

    # Return existing session if already created
    if CACHED_SESSION:
        return CACHED_SESSION

    # Authenticate, cache session and return it
    CACHED_SESSION = session.Session(auth=authenticate(output=output))
    return CACHED_SESSION


def invalidate_session():
    global CACHED_SESSION
    if CACHED_SESSION:
        CACHED_SESSION.invalidate()

def authenticate(output=False):
    """
    Authenticates and returns a password auth plugin object.
    We are scoping to a project, something you want to do in 99% of the use cases.
    """
    if output:
        print "=== Authenticating: Project scoped ==="
        print "OS_AUTH_URL", os.getenv('OS_AUTH_URL')
        print "OS_USERNAME", os.getenv('OS_USERNAME')
        print "OS_USER_DOMAIN_NAME", os.getenv('OS_USER_DOMAIN_NAME')
        print "OS_PROJECT_DOMAIN_NAME", os.getenv('OS_PROJECT_DOMAIN_NAME')

    return v3.Password(auth_url=os.getenv('OS_AUTH_URL'),
                       # Credentials
                       username=os.getenv('OS_USERNAME'),
                       password=os.getenv('OS_PASSWORD'),
                       # The domain our user is authenticating with
                       user_domain_name=os.getenv('OS_USER_DOMAIN_NAME'),
                       # project_domain_name: we scope to a project in the domain
                       project_domain_name=os.getenv('OS_PROJECT_DOMAIN_NAME'),
                       project_name=os.getenv('OS_PROJECT_NAME'),
                       # Automatically re-authenticate if the token expires
                       reauthenticate=True,
                       include_catalog=True)


def get_client():
    return keystone_client.Client(session=get_session())


def get_session_info(output=False):
    session = get_session(output=True)
    print "=== Session Information ==="
    print "Domain     :", session.auth.project_domain_name
    print "Project ID :", session.get_project_id()
    print "User ID    :", session.get_user_id()
    print "Raw Token  :", session.get_token() 
    return {}


def project_list():
    client = get_client()
    print client.projects.list()


def main():
    get_session_info()
    project_list()

if __name__ == '__main__':
    main()
