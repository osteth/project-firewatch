# Skeleton of a CLI

import click

import project-firewatch


@click.command('project-firewatch')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(project-firewatch.has_legs)
