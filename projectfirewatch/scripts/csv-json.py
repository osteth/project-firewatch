#!/usr/bin/python

import csv
import json
import click


@click.group()

def cli(*args, **kwargs):
    """Command line utility to easily convert .csv data over to .json data.  This utility was built for the NASA space apps challenge and is defaulted 
	to be used with cron to pull in data from https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data convert it to json 
	and load it into a database to overcome the lack of a useable api for this data.
	Usage: python3 csv-json.py convert -i <input file path> -o <output file path>"""
    pass

@click.command(help='Covert data from csv to json.')
@click.option('--input', '-i', default='MODIS_C6_Global_24h.csv', help='--input , -i	Sets the file that is to be converted')
@click.option('--output', '-o', default='MODIS_C6_Global_24h.json', help='--output, -o,   Sets the name of the output.')
def convert(input, output):


	csvfile = open(input, 'r')
	jsonfile = open(output, 'w')

	reader = csv.DictReader( csvfile)
	for row in reader:
		json.dump(row, jsonfile)
		jsonfile.write('\n')


cli.add_command(convert)

if __name__ == '__main__':
	cli()
