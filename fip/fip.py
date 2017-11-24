""" Fip module

This module manages the Fip class in order to request the data and save them.

Todo:
    - Improve docstrings
    - Log eventually events
    - Add an authentification system in another file or here

"""

import requests


class Fip():
    """ Fip class

    Instanciate an object that will request data from Fip server

    """

    def __init__(self):
        """ Constructor of the Fip class

        Initialize the instance

        """
        self.url = 'http://www.fipradio.fr/livemeta/7'
        self.data = {}
        self.uid = []

    def request_data(self, offset=0):
        """ Request the data to the server

        Send a request to the server to grab a specific JSON file containing
        the information related to lastest songs played on the radio.

        Args:
            offset (int):   Offset to grab the next song information (but could
                            be the previous too).

        """
        data = requests.get(self.url).json()
        level = data['levels'][0]
        position = level['position'] + offset
        self.uid = level['items'][position]
        self.data = data['steps'][self.uid]

    def save_data(self):
        return NotImplemented
