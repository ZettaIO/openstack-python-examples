"""
Compute/Nova examples
"""
from novaclient import client
import identity

def get_client():
    """
    Create a nova (version 2) client using a session
    """
    return client.Client(2, session=identity.get_session())

def instance_list():
    """
    Fetch a list containing all virtual machines / instances
    running in your project.
    """
    compute = get_client()
    instances = compute.servers.list()

    print "=== Instance list ({}) ===".format(len(instances))
    for instance in instances:
        print " -> ({}) {}".format(instance.id, instance.name)
        print instance.to_dict()
    if len(instances) == 0:
        print "No instances ;_;"

    return instances

def flavor_list():
    """
    Lists all supported flavors for instances.
    """
    compute = get_client()
    flavors = compute.flavors.list()
    print "=== Flavors ==="
    for flavor in flavors:
        print "- > ({}) {}".format(flavor.id, flavor.name)

    

#instance_list()
#flavor_list()
