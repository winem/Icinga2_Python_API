import json
import urllib3
from requests import Session

class Icinga2APIClient(object):
    """
    Main Class to implement the Icinga2 API Client
    """

    URLCHOICES = {
        "host": "/v1/objects/hosts",
        "hostgroup": "/v1/objects/hostgroups",
        "service": "/v1/objects/services",
        "servicegroup": "/v1/objects/servicegroups",
        "notification": "/v1/objects/notifications",
        "downtime": "/v1/objects/downtimes"
    }

    def __init__(self):
        """
        Initialize all needed Variables
        """

        self.connection = Session()
        self.connection.headers.update({'Accept': 'application/json'})
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def setconfig(self, username=None, password=None, url=None):
        if url is not None:
            self.url = url
        else:
            raise ValueError("No URL set")

        self.connection.auth = (username, password)

    def get_Data(self, type):
        """
        Get Data from icinga2
        """

        ret = self.connection.get(self.url + self.URLCHOICES[type], verify=False)
        ret.raise_for_status()
        return json.loads(ret.text)

    def delete_Data(self, type, name):
        """
        Get Data from icinga2
        """

        ret = self.connection.delete(self.url + self.URLCHOICES[type] + name, verify=False)
        ret.raise_for_status()
        return json.loads(ret.text)

    def put_Data(self, type, data):
        """
        Put Data into Icinga2 via the API

        :param type: type of uri to attach to url
        :param data: Data Dictionary that is used to add values to Icinga2
        """
        ret = self.connection.put(self.url + self.URLCHOICES[type] + data['name'], data=json.dumps(data), verify=False)
        ret.raise_for_status()

    def post_Data(self, type, data):
        """
        POST method
        :param type: type of uri to attach to url
        :param data: Data Dictionary that is used to query the Icinga2API
        """
        ret = self.connection.post(self.url + self.URLCHOICES[type], headers={'X-HTTP-Method-Override': 'GET'}, data=json.dumps(data), verify=False)
        ret.raise_for_status()
        return json.loads(ret.text)
