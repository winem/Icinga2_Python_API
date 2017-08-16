from . import client
class Servicegroups():
    """
    Class that contains all informations about Servicegroups and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        if config:
            self.config = config

    def add(self, servicegroupdata=None):
        """
        To be filled
        """
        pass

    def delete(self, servicegroupname=None):
        """
        To be filled
        """
        pass

    def list(self, servicegroupname=None):
        """
        To be filled
        """
        pass

    def exists(self, servicegroupname=None):
        """
        To be filled
        """
        pass
