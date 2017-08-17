from lib import client, downtime, host, hostgroups, notifications, service, servicegroups, usergroups, users
from pprint import pprint

class Icinga2API(object):
    """
    Main Class to implement the Icinga2 API
    """

    def __init__(self, username=None, password=None, url=None):
        """
        Initialize all needed Classes
        """

        self.client = client.Icinga2APIClient()
        self.client.setconfig(username, password, url)
        self.downtime = downtime.Downtime(client=self.client)
        self.host = host.Host(client=self.client)
        self.hostgroup = hostgroups.Hostgroup(client=self.client)
        self.notification = notifications.Notification(client=self.client)
        self.service = service.Service(client=self.client)
        self.servicegroup = servicegroups.Servicegroups(client=self.client)
        self.usergroup = usergroups.Usergroups(client=self.client)
        self.user = users.Users(client=self.client)


if __name__ == '__main__':
    api = Icinga2API(username="root", password="1a15f273bf8c908d", url="https://icinga.mw-krz-swd.de:5665")
    pprint(api.host.problem_list())
