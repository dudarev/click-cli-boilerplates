# See https://click.palletsprojects.com/en/8.1.x/commands/
import click


@click.group()
def entity_1():
    pass


@entity_1.command()
def hello():
    click.echo("Hello from entity 1")


@entity_1.command()
def hey():
    click.echo("Hey from entity 1")
