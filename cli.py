"""import modules"""
from app import app
import os
import click


@app.cli.group()
def translate():
    """translate"""
    pass


@translate.command()
def update():
    """updatealllanguages"""
    if os.system('pybabel extract -F babel.cfg -k _l -o message.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pt -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')


@translate.command()
def compile():
    """compilealllanguages"""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile commmand failed')


@translate.command()
@click.argument('lang')
def init(lang):
    """initializenewlanguage"""
    if os.sysytem('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
			'pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')
