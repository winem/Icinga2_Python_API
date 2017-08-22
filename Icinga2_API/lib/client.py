from requests import Session
import urllib3
import logging
import json

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

        self.log = logging.getLogger('Icinga2API.client')
        self.connection = Session()
        self.connection.headers.update({'Accept': 'application/json'})
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def setconfig(self, username=None, password=None, url=None):
        if url is not None:
            self.baseurl = url
        else:
            raise ValueError("No URL set")

        self.connection.auth = (username, password)

    def get_Data(self, url):
        """
        Get Data from icinga2
        """
        try:
            ret = self.connection.get(self.baseurl + url, verify=False)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise

    def delete_Data(self, url):
        """
        Delete Data from icinga2
        """

        try:
            ret = self.connection.get(self.baseurl + url, verify=False)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise

    def put_Data(self, url):
        """
        Put Data into Icinga2 via the API

        :param type: type of uri to attach to url
        :param data: Data Dictionary that is used to add values to Icinga2
        """
        try:
            ret.raise_for_status()
            ret = self.connection.put(self.baseurl + url, data=json.dumps(data), verify=False)
        except Exception as e:
            self.log.error(e)
            raise

    def post_Data(self, url, data):
        """
        POST method
        :param type: type of uri to attach to url
        :param data: Data Dictionary that is used to query the Icinga2API
        """
        try:
            ret = self.connection.post(self.baseurl + url, headers={'X-HTTP-Method-Override': 'GET'}, data=json.dumps(data), verify=False)
            ret.raise_for_status()
            return json.loads(ret.text)
        except Exception as e:
            self.log.error(e)
            raise
