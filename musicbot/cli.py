#!/usr/bin/env python3
import click
import click_completion
import os
import logging
from click_repl import register_repl
from attrdict import AttrDict
from musicbot import helpers, config

bin_folder = os.path.dirname(__file__)
commands_folder = 'commands'
plugin_folder = os.path.join(bin_folder, commands_folder)
CONTEXT_SETTINGS = {'auto_envvar_prefix': 'MB', 'help_option_names': ['-h', '--help']}
logger = logging.getLogger('musicbot')


def custom_startswith(string, incomplete):
    """A custom completion matching that supports case insensitive matching"""
    if os.getenv('_MUSICBOT_CASE_INSENSITIVE_COMPLETE', False):
        string = string.lower()
        incomplete = incomplete.lower()
    return string.startswith(incomplete)


click_completion.startswith = custom_startswith
click_completion.init()


class SubCommandLineInterface(helpers.GroupWithHelp):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and '__init__' not in filename:
                rv.append(filename[:-3])
        all_commands = rv + super().list_commands(ctx)
        all_commands.sort()
        return all_commands

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        try:
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                ns['__name__'] = '{}.{}'.format(commands_folder, name)
                ns['__file__'] = fn
                eval(code, ns, ns)
        except FileNotFoundError:
            return super().get_command(ctx, name)
        return ns['cli']


@click.group(cls=SubCommandLineInterface, context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.version_option("1.0", "--version", "-V")
@helpers.add_options(config.options)
@click.pass_context
def cli(ctx, **kwargs):
    """Music swiss knife, new gen."""
    ctx.obj = AttrDict
    ctx.obj.folder = bin_folder
    config.config.set(**kwargs)
    ctx.obj.config = config.config


def main(**kwargs):
    register_repl(cli)
    return cli.main(**kwargs)


if __name__ == '__main__':
    main()
