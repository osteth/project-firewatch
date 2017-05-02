# coding: utf-8
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
#FlaskAPI docs avilable at http://www.flaskapi.org/
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import json

app = FlaskAPI(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyByCF9JlHWGthilogp3Q-Y1qiNaqRtZ6ZQ"

# you can also pass key here
GoogleMaps(app, key="AIzaSyByCF9JlHWGthilogp3Q-Y1qiNaqRtZ6ZQ")

def LLR():
    llr_dict = {}

	# Reading data back
    with open('MODIS_C6_Global_24h.json') as json_file:
        for string in json_file:
            data = json.loads(string)
            lon = float(data['longitude'])
            lat = float(data['latitude'])
            scan = data['scan']
            track = data['track']
            radius = round((float(scan) * float(track) / 2) * 750, 2) #kilometers rounded to two decimal places 
            stroke_color = "FF0000"
            fill_color = "FF0000"
            llr_dict.update({'stroke_color': 'FF0000',
            'fill_color': 'FF0000',
            'center': {'longitude': lon,
            'latitude': lat},
            'radius': radius,
            'infobox': 'Activate Fire Area as reporterd'})
    '''for i in llr_dict:
        print (i, llr_dict[i])
            #print(stroke_color,fill_color,lon,lat,radius)'''
    return llr_dict

@app.route("/api/", methods=['GET', 'POST'])
def Dump_sat():
	'''
	curl -H "Content-Type: application/json" -X POST -d '{"TeamID": "Mudkips","IP": "192.168.0.1","Port": "5001"}' http://localhost:5001/checkin/
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
	
@app.route('/fullmap')
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
                'lat': 34.713811,
                'lng': -86.594352
            },
            'radius': 200,
            'infobox': "This is a circle"
        }],
        maptype = "TERRAIN",
        zoom="16"
    )
    return render_template('example_fullmap.html', fullmap=fullmap)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True, use_reloader=True)
