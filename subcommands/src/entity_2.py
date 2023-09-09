# See https://click.palletsprojects.com/en/8.1.x/commands/
import click


@click.group()
def entity_2():
    pass


@entity_2.command()
def hello():
    click.echo("Hello from entity 2")
