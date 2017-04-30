#!/bin/bash

#get file from nasa and overwrite old file
curl https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_Global_24h.csv > MODIS_C6_Global_24h.csv

#convert csv to json
./csv-json.py convert
