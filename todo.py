import click
from db import usedb
import random

@click.command()
@click.option("--add", help="add elements to the todo list")
@click.option("--delete", help="delete elements from the todo")
def cli(add, delete):
    if add and delete is None:
        click.echo(usedb(True, False, [random.randint(0, 1000), add]))
    elif add and delete:
        click.echo(usedb(True, True, [random.randint(0, 1000), add], delete))
    elif delete and add is None:
        click.echo(usedb(False, True, None, delete))
    else:
        for n in usedb():
            click.echo(n)
