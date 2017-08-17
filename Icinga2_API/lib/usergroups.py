from . import client
class Usergroups():
    """
    Class that contains all informations about Usergroups and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        if config:
            self.config = config

    def add(self, usergroupdata=None):
        """
        To be filled
        """
        pass

    def delete(self, usergroupname=None):
        """
        To be filled
        """
        pass

    def list(self, usergroupname=None):
        """
        To be filled
        """
        pass

    def exists(self, usergroupname=None):
        """
        To be filled
        """
        pass
