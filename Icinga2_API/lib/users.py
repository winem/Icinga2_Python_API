from . import client
class Users():
    """
    Class that contains all informations about users and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        if config:
            self.config = config

    def add(self, userdata=None):
        """
        To be filled
        """
        pass

    def delete(self, username=None):
        """
        To be filled
        """
        pass

    def list(self, username=None):
        """
        To be filled
        """
        pass

    def exists(self, username=None):
        """
        To be filled
        """
        pass
