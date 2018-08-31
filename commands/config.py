# -*- coding: utf-8 -*-
import click
from lib import helpers, database, server, persistence
from lib.config import config
from click_didyoumean import DYMGroup
from logging_tree import printout


@click.group(cls=DYMGroup)
def cli():
    '''Config management'''


@cli.command()
def show():
    print(config)


@cli.command()
@helpers.coro
@helpers.add_options(persistence.options)
@helpers.add_options(database.options)
@helpers.add_options(server.options)
async def save(**kwargs):
    '''Save config'''
    redis = persistence.Persistence(**kwargs)
    await redis.connect()
    await redis.execute('set', 'my-key', 'value')
    val = await redis.execute('get', 'my-key')
    print(val)
    await redis.close()


@cli.command()
def logging():
    printout()
