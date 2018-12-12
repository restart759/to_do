# -*-coding: utf-8 -*-

import click

from app import app, db

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create db after drop.')
def initdb(drop):
	if drop:
		click.confirm('are you sure to delete your db?', abort = True)
		db.drop_all()
		click.echo('Drop db.')
	db.create_all()
	click.echo('Initialize db.')
