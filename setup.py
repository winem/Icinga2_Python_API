import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'Icinga2 API',
  packages = ['Icinga2_API'], # this must be the same as the name above
  version = '0.1',
  description = 'An enhanced API to communicate with Icinga2',
  author = 'Kevin Honka',
  author_email = 'kevin.honka@astosch.de',
  url = 'https://git.astosch.de/kevin.honka/Icinga2_Python_API', # use the URL to the github repo
  download_url = 'https://git.astosch.de/kevin.honka/Icinga2_Python_API/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['Icinga2', 'API'], # arbitrary keywords
  classifiers = [],
)
