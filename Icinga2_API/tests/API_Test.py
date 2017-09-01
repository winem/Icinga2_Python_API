from nose.tools import assert_true, assert_is_not_none
import urllib3
import requests
from ..icinga2 import Icinga2API

def test_host_objects():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get("https://root:1a15f273bf8c908d@icinga.mw-krz-swd.de:5665/v1/objects/hostgroups", verify=False)
    assert_true(response.ok)
