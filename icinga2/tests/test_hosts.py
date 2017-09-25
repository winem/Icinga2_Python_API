import urllib3
import pytest
import copy
from icinga2 import Icinga2API
import Constants

def test_host_add():
    """
    Testing the addition of a host
    """
    api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url, debug=True)

    data = copy.deepcopy(Constants.TestHost_data)

    response = api.hosts.add(data)

    assert response['results'][0]['code'] == 200

def test_host_exists():
    """
    Testing if the host was added correctly
    """
    api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url, debug=True)

    response = api.hosts.exists(Constants.TestHost_data['attrs']['name'])

    assert response

def test_host_list():
    """
    Listing all Hosts, and check if created host is present
    """
    api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url, debug=True)

    response = api.hosts.list()

    assert Constants.TestHost_data['attrs']['name'] in response

def test_host_objects():
    """
    Get all Host Objects and check if created host is present
    """
    api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url, debug=True)

    response = api.hosts.objects()

    assert any(res.get('name', None) == Constants.TestHost_data['attrs']['name'] for res in response)

def test_host_delete():
    """
    Delete the created Host
    """
    api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url, debug=True)

    response = api.hosts.delete(Constants.TestHost_data['attrs']['name'])

    assert response != None
