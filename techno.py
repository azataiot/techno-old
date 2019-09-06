import click
import os
import time
import sys
from pyfiglet import Figlet
f = Figlet()
azt_welcome = f.renderText('AzatAI')

__author__ = "Oyetoke Toby"
__email__ = "a@azat.ai"
__copyright__ = "Azat Artificial Intelligence, LLP."



@click.command()
def cli():
    click.echo(azt_welcome)
    click.echo('Technopark Raspberry IoT Control Interface\nCopyright:2019 Azat Artificial Intelligence\n...Al-Farabi Kazakh National University...')



if __name__ == '__main__':
    cli()