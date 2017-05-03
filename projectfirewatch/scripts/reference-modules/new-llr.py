#!/usr/bin/python3


import json

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
		llr_table.append([
		'stroke_color' : stroke_color,
		'fill_color' : fill_color,
		'center': {'longitude': lon,
		'latitude': lat},
		'radius': radius,
		'infobox': 'Activate Fire Area as reported'])
	return(llr_table)


LLRTABLE = LLR()

print(len(LLRTABLE))	


#print(LLRTABLE[0])
i = 0
while i < len(LLRTABLE):
	print(LLRTABLE[i])
	i+=1






