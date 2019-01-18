import click
from db import usedb
import random

@click.command()
@click.option("--add", help="add elements to the todo list")
@click.option("--delete", help="delete elements from the todo")
def cli(add, delete):
    result = ""
    if add and delete is None:
        result = usedb(True, False, [random.randint(0, 1000), add])
    elif add and delete:
        result = usedb(True, True, [random.randint(0, 1000), add], delete)
    elif delete and add is None:
        result = usedb(False, True, None, delete)
    else:
        result = usedb()
    for n in result:
        print(f"{n[1]} - {n[0]}")
