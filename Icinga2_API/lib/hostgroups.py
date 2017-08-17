from . import client
class Hostgroup():
    """
    Class that contains all informations about Hostgroups and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        if config:
            self.config = config

    def add(self, hostgroupdata=None):
        """
        To be filled
        """
        pass

    def delete(self, hostgroupname=None):
        """
        To be filled
        """
        pass

    def list(self, hostgroupname=None):
        """
        To be filled
        """
        pass

    def exists(self, hostgroupname=None):
        """
        To be filled
        """
        pass
