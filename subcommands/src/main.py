import click

from .entity_1 import entity_1
from .entity_2 import entity_2


@click.group()
def cli():
    pass


cli.add_command(entity_1)
cli.add_command(entity_2)
