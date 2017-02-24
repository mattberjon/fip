import requests


class Fip():

    def __init__(self):
        self.url = 'http://www.fipradio.fr/livemeta/7'
        self.data = {}
        self.uid = []

    def request_data(self, offset=0):
        data = requests.get(self.url).json()
        level = data['levels'][0]
        position = level['position'] + offset
        self.uid = level['items'][position]
        self.data = data['steps'][self.uid]

    def save_data(self):
        pass
