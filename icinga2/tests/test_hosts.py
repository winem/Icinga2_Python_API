from __future__ import absolute_import

import copy

from icinga2 import Icinga2API
from .constants import constants


def test_host_add():
    """
    Testing the addition of a host
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

    data = copy.deepcopy(constants.TestHost_data)

    response = api.hosts.add(data)

    assert response['results'][0]['code'] == 200

def test_host_exists():
    """
    Testing if the host was added correctly
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

    response = api.hosts.exists(constants.TestHost_data['attrs']['name'])

    assert response

def test_host_list():
    """
    Listing all Hosts, and check if created host is present
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

    response = api.hosts.list()

    assert constants.TestHost_data['attrs']['name'] in response

def test_host_objects():
    """
    Get all Host Objects and check if created host is present
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

    response = api.hosts.objects()

    assert any(res.get('name', None) == constants.TestHost_data['attrs']['name'] for res in response)

def test_host_delete():
    """
    Delete the created Host
    """
    api = Icinga2API(username=constants.username, password=constants.password, url=constants.url, debug=True)

    response = api.hosts.delete(constants.TestHost_data['attrs']['name'])

    assert response != None
