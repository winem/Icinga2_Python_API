from . import client
class Service():
    """
    Class that contains all informations about Services and corresponding funtions
    """

    def __init__(self, config=None, client=None):
        """
        Initialize the Object with a given set of configurations.
        """
        if config:
            self.config = config

    def add(self, servicedata=None):
        """
        To be filled
        """
        pass

    def delete(self, servicename=None):
        """
        To be filled
        """
        pass

    def list(self, servicename=None):
        """
        To be filled
        """
        pass

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
