from . import client
class Host():
    """
    Class that contains all informations about Hosts and corresponding funtions
    """

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
        To be filled
        """
        pass

    def delete(self, hostname=None):
        """
        To be filled
        """
        pass

    def list(self, hostname=None):
        """
        To be filled
        """
        if hostname is not None:
            host_filter = {
                "filter": "host.name == name",
                "filter_vars": {
                    "name": hostname
                }
            }
            return self.client.post_Data(self.filter, host_filter)
        else:
            return self.client.get_Data(self.filter)

    def exists(self, hostname=None):
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

    def critical_count(self, arg):
        """
        To be filled
        """
        pass

    def down_count(self, arg):
        """
        To be filled
        """
        pass

    def unknown_count(self, arg):
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
