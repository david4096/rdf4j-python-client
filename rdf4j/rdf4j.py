"""
This file contains a client for interacting with the RDF4J ReST API using a
Python DSL.

Usage:

c = rdf4j.client("localhost")
protocol_version = c.protocol()
statements = c.statements()
my_repo = c.repo('my_repo')

"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests

class client(object):
    """
    Provides methods to interact with RDF4J ReST API.
    """
    def __init__(self, url, port=8080, base_path='rdf4j-server', log_level=0):
        self._page_size = None
        # FIXME why unicode?
        self._base_path = base_path
        self._port = port
        self._url = str(url)
        self._log_level = log_level
        self._protocol_bytes_received = 0
        logging.basicConfig()
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(log_level)

    def prefix(self):
        return "http://{}:{}/{}/".format(self._url, self._port, self._base_path)

    def make_url(self, fragments):
        print("fragments", fragments)
        suffix = "/".join(fragments)
        print(suffix)
        print(self.prefix() + suffix)
        return self.prefix() + suffix

    def get(self, paths):
        return requests.get(self.make_url(paths))

    def protocol(self):
        """
        Returns the protocol version of the server as a string.

        :return: String protocol version
        """
        self._logger.debug("protocol")
        return self.get(["protocol"]).text

    def repositories(self):
        """
        Returns a list of the repository names in the RDF4J instance.

        :return:
        """


    def statements(self):
        """

        :return:
        """

    def context(self):
        """

        :return:
        """

    def size(self):
        """

        :return:
        """

    def rdf_graphs(self):
        """

        :return:
        """

    def service(self):
        """

        :return:
        """

    def namespaces(self):
        """

        :return:
        """

    def transactions(self):
        """

        :return:
        """