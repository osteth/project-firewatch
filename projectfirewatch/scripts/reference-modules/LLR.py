#!/usr/bin/env python3

import json

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
			radius = (float(scan) * float(track) / 2) * 750 #kilometers
			radius = round(radius, 2) #round to two decimal places
			stroke_color = "FF0000"
			fill_color = "FF0000"
			llr_dict.update({'stroke_color': 'FF0000',
			'fill_color': 'FF0000',
			'center': {'longitude': lon,
			'latitude': lat},
			'radius': radius,
			'infobox': 'Activate Fire Area as reporterd'})
	"""for i in llr_dict:
		print (i, llr_dict[i])
			#print(stroke_color,fill_color,lon,lat,radius)"""
	return(llr_dict)

if __name__ == "__main__":
	LLR()
