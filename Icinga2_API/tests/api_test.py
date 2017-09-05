import urllib3
import pytest
import copy
from ..icinga2 import Icinga2API
from Constants import Constants

class api_test():

    def test_host_add(self):
        """
        Testing the addition of a host
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url, debug=True)

        data = copy.deepcopy(Constants.TestHost_data)

        response = self.api.host.add(data)

        assert response['results'][0]['code'] == 200

    def test_host_exists(self):
        """
        Testing if the host was added correctly
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url)

        response = self.api.host.exists(Constants.TestHost_data['attrs']['name'])

        assert response

    def test_host_list(self):
        """
        Listing all Hosts, and check if created host is present
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url)

        response = self.api.host.list()

        assert Constants.TestHost_data['attrs']['name'] in response

    def test_host_objects(self):
        """
        Get all Host Objects and check if created host is present
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url)

        response = self.api.host.objects()

        assert any(res.get('name', None) == Constants.TestHost_data['attrs']['name'] for res in response)

    def test_host_delete(self):
        """
        Delete the created Host
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.api = Icinga2API(username=Constants.username,password=Constants.password,url=Constants.url)

        response = self.api.host.delete(Constants.TestHost_data['attrs']['name'])

        assert response != None
