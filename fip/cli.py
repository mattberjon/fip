# -*- coding: utf-8 -*-

from . import __version__
import click
import sys
from datetime import datetime
from . import fip


def version_msg():
    """ Returns the program version, location and python version
    """
    python_version = sys.version[:3]
    message = 'FIP %(version)s (Python {})'
    return message.format(python_version)


def display(data):

    if data.get('title'):
        title = "Title: {0}".format(data.get('title'))
        print(title)

    if data.get('authors'):
        artist = "Artist: {0}".format(data['authors'])
        print(artist)

    if data.get('titreAlbum'):
        album = "Album: {0} ({1})".format(
                data.get('titreAlbum'),
                data.get('anneeEditionMusique'))
        print(album)

    if data.get('label'):
        label = "Label: {0}".format(data.get('label'))
        print(label)

    if data.get('start'):
        start = "Starts at: {0}".format(date_from_timestamp(data.get('start')))
        print('------')
        print(start)

    if data.get('end'):
        stop = "Stops at: {0}".format(date_from_timestamp(data.get('end')))
        print(stop)


def date_from_timestamp(timestamp):
    date = datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
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
        data = fip.Fip()
        data.request_data()
        display(data.data)
    elif next_song:
        data = fip.Fip()
        data.request_data(offset=1)
        display(data.data)


if __name__ == "__main__":
    main()
