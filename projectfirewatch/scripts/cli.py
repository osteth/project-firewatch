# coding: utf-8
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
#FlaskAPI docs avilable at http://www.flaskapi.org/
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import json
import csv
import click
import wget
import os

port = 5000
debug = True
reload = True
path = os.path.realpath(__file__).replace(__file__, '')
print(path)
app = FlaskAPI(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyByCF9JlHWGthilogp3Q-Y1qiNaqRtZ6ZQ"

# you can also pass key here
GoogleMaps(app, key="AIzaSyByCF9JlHWGthilogp3Q-Y1qiNaqRtZ6ZQ")

#begin CLI  Portion
@click.group()
def cli(*args, **kwargs):
    """Command line utility to easily convert .csv data over to .json data.  This utility was built for the NASA space apps challenge and is defaulted 
	to be used with cron to pull in data from https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data convert it to json 
	and load it into a database to overcome the lack of a useable api for this data.
	Usage: python3 csv-json.py convert -i <input file path> -o <output file path>"""
    pass

@click.command(help='Retrieves MODIS satelite CSV data and coverts data from csv to json.')
@click.option('--input', '-i', default=path + 'MODIS_C6_Global_24h.csv', help='--input , -i	Sets the file that is to be converted')
@click.option('--output', '-o', default=path + 'MODIS_C6_Global_24h.json', help='--output, -o,   Sets the name of the output.')
def update(input, output):
	try:
		os.remove(path + 'MODIS_C6_Global_24h.json')
	except OSError:
		pass
	MODISurl = 'https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_Global_24h.csv'	
	filename = wget.download(MODISurl, path)
	
	csvfile = open(input, 'r')
	jsonfile = open(output, 'w')

	reader = csv.DictReader( csvfile)
	for row in reader:
		json.dump(row, jsonfile)
		jsonfile.write('\n')
	
	try:
		os.remove(path + 'MODIS_C6_Global_24h.csv')
	except OSError:
		pass

	return(filename)

@click.command(help='Start/Stop the mapping and API server.')
def start():
	app.run(host='0.0.0.0',port=port,debug=debug, use_reloader=reload)
	
	return('Server Started')

cli.add_command(update)
cli.add_command(start)

#End CLI portion

#begin Auxiliary Functions
def LLR():
	table = []
	llr_table = []

	with open('MODIS_C6_Global_24h.json', 'r') as data_file:
		for line in data_file:
			try:
				j = line.split('|')[-1]
				table.append(json.loads(j))
			except ValueError:
				print("Bad Json File!")
				continue

	for row in table:
		lon = float(row['longitude'])
		lat = float(row['latitude'])
		scan = row['scan']
		track = row['track']
		radius = (float(scan) * float(track) / 2) * 750 #kilometers
		radius = round(radius, 2) #round to two decimal places
		stroke_color = "FF0000"
		fill_color = "FF0000"
		llr_table.append({
		'center': {'longitude': lon,
		'latitude': lat},
		'radius': radius,
		'infobox': 'Activate Fire Area as reported'})
	return(llr_table)
	
#End Auxilary Functions

#Begin API
@app.route("/api/", methods=['GET', 'POST'])
def Dump_sat():
	'''
	dumps all MODIS data in JSON format.
	'''

	SatDataTable = []

	with open('MODIS_C6_Global_24h.json', 'r') as SatData:
		for line in SatData:
			try:
				j = line.split('|')[-1]
				SatDataTable.append(json.loads(j))
			except ValueError:
				print("Bad Json File!")
				continue


	return {"Satellite Data": SatDataTable}

	
#End API

#Bgin Map
@app.route('/')
def fullmap():
    firedata = LLR()
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=34.715820,
        lng=-86.597105,
        markers=[
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 34.716769,
                'lng': -86.597240,
                'infobox': "Sensor: 1, Temp: 86, humidity: 46% ALERT: False"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 34.716323,
                'lng': -86.594007,
                'infobox': "Sensor: 2, Temp: 86, humidity: 46% ALERT: False"
            },
			{
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 34.715508,
                'lng': -86.598972,
                'infobox': "Sensor: 3, Temp: 86, humidity: 46% ALERT: False"
            },
			{
                'icon': '//maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                'lat': 34.714402,
                'lng': -86.599079,
                'infobox': "Sensor: 4, Temp: 124, humidity: 8% ALERT: Upcoming Alert Probable"
            },
			{
                'icon': '//maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat': 34.713745,
                'lng': -86.597834,
                'infobox': "Sensor: 5, Temp: overload, humidity: 0% ALERT: TRUE"
            },
			{
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 334.713767,
                'lng': -86.596396,
                'infobox': "Sensor: 6, Temp: 86, humidity: 46% ALERT: False"
            },
			{
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 34.713811,
                'lng': -86.594352,
                'infobox': "Sensor: 7, Temp: 86, humidity: 46% ALERT: False"
            }
        ],
        circles=[{
            'stroke_color': '#FF00FF',
            'stroke_opacity': 1.0,
            'stroke_weight': 7,
            'fill_color': '#FF00FF',
            'fill_opacity': 0.2,
            'center': {
                'lat': 34.715709,
                'lng':  -86.597161
            },
            'radius': 100,
            'infobox': "Active Wildfire Area reported by MODIS satellite"
        }],
        maptype = "TERRAIN",
        zoom="16"
    )
    return render_template('example_fullmap.html', fullmap=fullmap)

#End Map

if __name__ == "__main__":
    cli()
