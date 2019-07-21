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
        self.url ='https://www.fip.fr/latest/api/graphql?operationName=Now&variables={%22bannerPreset%22%3A%22600x600-noTransform%22%2C%22stationId%22%3A7%2C%22previousTrackLimit%22%3A3}&extensions={%22persistedQuery%22%3A{%22version%22%3A1%2C%22sha256Hash%22%3A%228a931c7d177ff69709a79f4c213bd2403f0c11836c560bc22da55628d8100df8%22}}'
        self.data = {}
        self.type = 'cur'
        self.uid = []
        self.artist = []
        self.title = []

    def get_data(self):
        """ Get the raw data from the server

        Send a request to the FIP server to grab a specific JSON file
        containing the information related to lastest songs played on the
        radio.

        Args: None

        Returns: None

        """
        self.data = requests.get(self.url).json()

    def get_current(self):
        """ Get the current data information

        Args: None

        Returns: None
        """
        self.data = self.data['data']['now']['song']
        self.type = 'cur'

    def get_next(self):
        """ Get the next data information

        Args: None

        Returns: None
        """
        self.data = self.data['data']['nextTracks'][0]
        self.type = 'next'

    def get_prev(self):
        """ Get the previous data information

        Args: None

        Returns: None
        """
        self.data = self.data['data']['previousTracks']['edges'][0]['node']
        self.type = 'prev'

    def get_artist(self):
        """ Get the artist

        Args: None

        Returns:
            (str) the artist name
        """
        if (self.type == 'cur'):
            return self.data['interpreters'][0]
        else:
            return self.data['title']

    def get_title(self):
        """ Get the title

        Args: None

        Returns:
            (str) the song name
        """
        if (self.type == 'cur'):
            return self.data['title']
        else:
            return self.data['subtitle']

    def get_album(self):
        """ Get the album name

        Args: None

        Returns:
            (str) the album name
        """
        data = self.data.get('album')
        if data:
            return self.data['album']
        else:
            return None

    def get_label(self):
        """ Get the label name

        Args: None

        Returns:
            (str) the label name
        """
        data = self.data.get('label')
        if data:
            return self.data['label']
        else:
            return None

    def save_data(self):
        return NotImplemented
