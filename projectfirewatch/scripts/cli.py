# Skeleton of a CLI

import click

import projectfirewatch


@click.command('projectfirewatch')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(projectfirewatch.has_legs)
