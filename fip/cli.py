# -*- coding: utf-8 -*-

from . import __version__
import click
import sys


def version_msg():
    """ Returns the program version, location and python version
    """
    python_version = sys.version[:3]
    message = 'FIP %(version)s (Python {})'
    return message.format(python_version)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option(
        '-c',
        '--current',
        is_flag=True,
        help='Display the current song information')
@click.option(
        '-n',
        '--next',
        is_flag=True,
        help='Display the next song information')
@click.option(
        '-s',
        '--store',
        is_flag=True,
        help='Save the current song information')
@click.version_option(
        __version__,
        '-V',
        '--version',
        message=version_msg(),
        help='Ouput the version of this application')
def main(current, next, save):
    """Console script for fip_music"""
    click.echo("Replace this message by putting your code into "
               "fip.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
