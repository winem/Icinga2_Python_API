import logging
from pprint import pformat
class Host():
    """
    Class that contains all informations about Hosts and corresponding funtions
    """

    HOST_STATUS = {
        "DOWN": 1,
        "CRITICAL": 2,
        "UNKNOWN": 3
    }

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        self.client = client
        if config:
            self.config = config

        self.filter = 'host'

    def add(self, hostdata=None):
        """
        Adding a Host with a given set of Attributes and/or Templates

        :param hostdata: Provides the needed variables to create a host.
        Example:
        data = {
            "template": [ "generic-host" ],
            "attrs": {
                "name": "testserver1",
                "address": "127.0.0.1",
                "check_command": "hostalive"
            }
        }
        """

        def validate_hostdata(hostdata):
            NEEDED_VALUES = ("name")

            for need in NEEDED_VALUES:
                if need in hostdata['attrs']:
                    pass
                else:
                    raise ValueError("Error in Hostdata, expected {} but was not found".format(need))

        if not hostdata:
            raise ValueError("HostData not set")
        else:
            validate_hostdata(hostdata)

        logging.debug("Adding host with the following data: {}".format(pformat(hostdata)))
        self.client.put_Data(self.filter, hostdata)


    def delete(self, hostname=None):
        """
        Delte a Host based on the hostname

        :param hostname: Hostname of the Host that is to be deleted
        """
        if not hostname:
            raise ValueError("Hostname not set")
        else:
            logging.debug("Deleting Host with name: {}".format(hostname))
            self.client.delete_Data(self.filter, hostname)

    def list(self, hostname=None):
        """
        Method to list all hosts or only a select one
        Returns a list of all Hosts

        :param hostname: can be used to only list one Host, if not set it will retrieve all Hosts
        """
        if hostname is not None:
            host_filter = {
                "attrs": ["name"],
                "filter": "host.name == name",
                "filter_vars": {
                    "name": hostname
                }
            }
        else:
            host_filter = {
                "attrs": ["name"]
            }

        logging.debug("Listing all Hosts that match: {}".format(pformat(host_filter)))
        ret = self.client.post_Data(self.filter, host_filter)

        return_list = []

        for attrs in ret['results']:
            return_list.append(attrs['name'])

        logging.debug("Finished list of all matches: {}".format(pformat(return_list)))
        return return_list


    def exists(self, hostname=None):
        """
        Method to check if a single host exists

        :param hostname: Is needed to check if the Host exists, will throw a Value Exception when not set
        """
        if hostname:
            result = self.list(hostname=hostname)

            if not result:
                return False
            else:
                return True
        else:
            raise ValueError("Hostname was not set")

    def objects(self, attrs=None, _filter=None, joins=None):
        """
        returns host objects that fit the filter and joins

        :attrs List: List of Attributes that are returned
        :_filter List: List of filters to be applied
        :joins List:
        """

        def problem_count(data, value):
            problems = 0

            for attrs in data:
                if attrs['attrs']['state'] == value:
                    problems += 1

            return problems

        payload = {}

        if attrs:
            payload['attrs'] = attrs
        else:
            payload['attrs'] = ['name', 'state', 'acknowledgement', 'downtime_depth', 'last_check']

        logging.debug("Attrs set to: {}".format(pformat(payload['attrs'])))

        if _filter:
            payload['filter'] = _filter
            logging.debug("Filter set to: {}".format(pformat(payload['filter'])))

        if joins:
            payload['joins'] = joins
            logging.debug("Joins set to: {}".format(pformat(payload['joins'])))

        logging.debug("Payload: {}".format(pformat(payload)))

        result = self.client.post_Data(self.filter, payload)

        logging.debug("Result: {}".format(result))

        if result['results']:
            self.problems_down = problem_count(result['results'], self.HOST_STATUS['DOWN'])
            self.problems_critical = problem_count(result['results'], self.HOST_STATUS['CRITICAL'])
            self.problems_unknown = problem_count(result['results'], self.HOST_STATUS['UNKNOWN'])

        return result['results']


    def adjusted(self, arg):
        """
        To be filled
        """
        handled_problems = self.problems_down + self.problems_unknown + self.problems_critical
        down_adjusted = self.hosts_down + handled_problems

        return (handled_problems, down_adjusted)


    def problem_count(self):
        """
        Return the count of hosts with problems that are neither acknowledged or have a downtime
        """
        count = 0

        host_data = self.objects()

        for data in host_data:
            if data['attrs']['downtime_depth'] == 0 and data['attrs']['acknowledgement'] == 0 and data['attrs']['state'] != 0:
                logging.debug("Found match for Host: {}".format(pformat(data['name'])))
                count += 1

        return count

    def problem_list(self):
        """
        Lists all Hosts and their severity count in a sorted order
        """

        host_problems = {}

        host_data = self.objects()

        for host in host_data:
            if host['attrs']['state'] != 0:
                host_problems[host['name']] = self.host_severity(host['attrs'])
                logging.debug("Calculated Severity for {} is {}".format(host['name'], host_problems[host['name']]))

        if len(host_problems) != 0:
            host_problems_severity = sorted(host_problems, reverse=True)
            return host_problems_severity
        else:
            return {}

    def severity(self, attrs):
        """
        Calculate the severity
        """

        def last_check(last_check_time):
            from datetime import datetime, timedelta

            last_check_time = datetime.fromtimestamp(last_check_time)
            now = datetime.now

            if now > last_check_time + timedelta(seconds=20):
                return False
            else:
                return True

        severity = 0

        logging.debug("calculating severity for {}".format(pformat(attrs['name'])))

        if attrs['acknowledgement'] != 0:
            severity += 2
        elif attrs['downtime_depth'] > 0:
            severity += 1
        else:
            severity += 4

        check_status = last_check()

        if check_status:
            severity += 16

        if attrs['state'] != 0:
            if attrs['state'] == 1:
                severity += 32
            elif attrs['state'] == 2:
                severity += 64
            else:
                severity += 256

        logging.debug("calculated severity for {} is {}".format(pformat(attrs['name']), severity))
        return severity
