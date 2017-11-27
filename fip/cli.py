# -*- coding: utf-8 -*-

from . import __version__
import click
import sys
from datetime import datetime
from .fip import Fip


def version_msg():
    """ Returns the program version, location and python version
    """
    python_version = sys.version[:3]
    message = 'FIP %(version)s (Python {})'
    return message.format(python_version)


def display(data):

    title = "Title: {0}".format(data.get_key('title'))
    print(title)

    artist = "Artist: {0}".format(data.get_key('authors'))
    print(artist)

    album = "Album: {0} ({1})".format(
            data.get_key('titreAlbum'),
            data.get_key('anneeEditionMusique'))
    print(album)

    label = "Label: {0}".format(data.get_key('label'))
    print(label)

    print('------')
    time = "The {0} at {1} until {2}".format(
            date_from_timestamp(data.get_key('start'), '%Y-%m-%d'),
            date_from_timestamp(data.get_key('start'), '%H:%M:%S'),
            date_from_timestamp(data.get_key('end'), '%H:%M:%S'))
    print(time)


def date_from_timestamp(timestamp, date_format='%Y-%m-%d %H:%M:%S'):
    date = datetime.fromtimestamp(int(timestamp)).strftime(date_format)
    return date


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option(
    '-c',
    '--current-song',
    is_flag=True,
    help='Display the current song information')
@click.option(
    '-n',
    '--next-song',
    is_flag=True,
    help='Display the next song information')
@click.option(
    '-s',
    '--save',
    is_flag=True,
    help='Save the current song information')
@click.version_option(
    __version__,
    '-V',
    '--version',
    message=version_msg(),
    help='Ouput the version of this application')
def main(current_song, next_song, save):
    if current_song:
        fip_data = Fip()
        fip_data.get_data()
        display(fip_data)
    elif next_song:
        data = Fip()
        data.request_data(offset=1)
        display(data.data)


if __name__ == "__main__":
    main()
