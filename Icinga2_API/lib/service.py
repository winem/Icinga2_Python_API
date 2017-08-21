from . import client
class Service():
    """
    Class that contains all informations about Services and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        self.client = client
        if config:
            self.config = config

        self.filter = 'service'
    def add(self, servicename, hostname, servicedata=None):
        """
        Adding a Service with a given set of Attributes and/or Templates

        :param servicedata: Provides the needed variables to create a service.
        Example:
        data = {
            "templates": [ "generic-service" ],
            "attrs": {
                "check_command": "ping4",
                "check_interval": 10,
                "retry_interval": 30
            }
        }
        """

        def validate_servicedata(servicedata):
            NEEDED_VALUES = ("check_command", "check_interval", "retry_interval")

            for need in NEEDED_VALUES:
                if need in servicedata['attrs']:
                    pass
                else:
                    raise ValueError("Error in Servicedata, expected {} but was not found".format(need))

        if not servicedata:
            raise ValueError("ServiceData not set")
        else:
            validate_hostdata(hostdata)

        logging.debug("Adding service with the following data: {}".format(pformat(servicedata)))
        self.client.put_Data(self.client.URLCHOICES[self.filter] + hostname + "!" + servicename, servicedata)

    def delete(self, hostname=None, servicename=None):
        """
        Delte a Service based on the hostname and servicename

        :param hostname: Hostname of the Host that is to be deleted
        """
        if not hostname and not servicename:
            raise ValueError("Hostname or Servicename not set")
        else:
            logging.debug("Deleting Host with name: {}".format(hostname))
            self.client.delete_Data(self.client.URLCHOICES[self.filter] + hostname + "!" + servicename)

    def list(self, hostname=None):
        """
        Method to list all services or only those for a single host

        :param hostname: can be used to only list one Host, if not set it will retrieve all Hosts
        """
        if hostname is not None:
            service_filter = {
                "attrs": ["name"],
                "joins": "host.name",
                "filter": "host.name == name",
                "filter_vars": {
                    "name": hostname
                }
            }
        else:
            service_filter = {
                "attrs": ["name"]
            }

        logging.debug("Listing all Hosts that match: {}".format(pformat(service_filter)))
        ret = self.client.post_Data(self.client.URLCHOICES[self.filter], service_filter)

        return_list = []

        for attrs in ret['results']:
            return_list.append(attrs['name'])

        logging.debug("Finished list of all matches: {}".format(pformat(return_list)))
        return return_list

    def unhandled_list(self, arg):
        """
        To be filled
        """
        pass

    def exists(self, servicename=None):
        """
        To be filled
        """
        pass

    def objects(self, filter=None):
        """
        To be filled
        """
        pass

    def adjusted(self, arg):
        """
        To be filled
        """
        pass

    def problem_count(self, arg):
        """
        To be filled
        """
        pass

    def warning_count(self, arg):
        """
        To be filled
        """
        pass

    def problem_handled_count(self, arg):
        """
        To be filled
        """
        pass

    def critical_count(self, arg):
        """
        To be filled
        """
        pass

    def critical_handled_count(self, arg):
        """
        To be filled
        """
        pass

    def unknown_count(self, arg):
        """
        To be filled
        """
        pass

    def unknown_handled_count(self, arg):
        """
        To be filled
        """
        pass

    def problem_list(self, arg):
        """
        To be filled
        """
        pass

    def problems(self, arg):
        """
        To be filled
        """
        pass

    def all_count(self, arg):
        """
        To be filled
        """
        pass

    def update_host(self, arg):
        """
        To be filled
        """
        pass
