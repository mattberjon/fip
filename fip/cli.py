# -*- coding: utf-8 -*-

from . import __version__
import click
import sys
from . import fip


def version_msg():
    """ Returns the program version, location and python version
    """
    python_version = sys.version[:3]
    message = 'FIP %(version)s (Python {})'
    return message.format(python_version)


def display(data):
    if data['title']:
        title = "Title: {0}".format(data['title'])
        print(title)

    if data['authors']:
        artist = "Artist: {0}".format(data['authors'])
        print(artist)

    if data['titreAlbum']:
        album = "Album: {0} ({1})".format(
                data['titreAlbum'],
                data['anneeEditionMusique'])
        print(album)

    if data['label']:
        label = "Label: {0}".format(data['label'])
        print(label)


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
