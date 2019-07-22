# -*- coding: utf-8 -*-

from . import __version__
import click
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from datetime import datetime
from .fip import Fip


def version_msg():
    """ Returns the program version, location and python version
    """
    python_version = sys.version[:3]
    message = 'FIP %(version)s (Python {})'
    return message.format(python_version)


def display(data):

    title = "Title: {0}".format(data.get_title())
    print(title)

    artist = "Artist: {0}".format(data.get_artist())
    print(artist)

    album = "Album: {0}".format(data.get_album())
    print(album)

    label = "Label: {0}".format(data.get_label())
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
    '-p',
    '--previous-song',
    is_flag=True,
    help='Display the previous song information')
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
def main(current_song, next_song, previous_song, save):
    if current_song:
        fip_data = Fip()
        fip_data.get_data()
        fip_data.get_current()
        display(fip_data)
    elif next_song:
        fip_data = Fip()
        fip_data.get_data()
        fip_data.get_next()
        display(fip_data)
    elif previous_song:
        fip_data = Fip()
        fip_data.get_data()
        fip_data.get_prev()
        display(fip_data)


if __name__ == "__main__":
    main()
