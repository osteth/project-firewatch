#!/usr/bin/python3

import sqlite3
import json

table = []

with open('MODIS_C6_Global_24h.json', 'r') as data_file:
    for line in data_file:
        try:
            j = line.split('|')[-1]
            table.append(json.loads(j))
        except ValueError:
            print("Bad Json File!")
            continue

# DB Creation Code, most likely functional

db = sqlite3.connect("nasa_data.db")
c = db.cursor()

c.execute('''create table nasa_data
         (
          latitude text,
          longitude text,
          brightness text,
          scan text,
          track text,
          acq_date text,
          acq_time text,
          satellite text,
          confidence text,
          version text, 
          bright_t31 text,
          frp text,
          daynight text)''')
    
query = "insert into nasa_data values (?,?,?,?,?,?,?,?,?,?,?,?,?)"


for row in table:
    mylist = [ row['latitude'], row['longitude'], row['brightness'], row['scan'], row['track'], row['acq_date'], row['acq_time'], row['satellite'], row['confidence'], row['version'], row['bright_t31'], row['frp'], row['daynight']]    
    c.execute(query, (mylist[0], mylist[1], mylist[2], mylist[3], mylist[4], mylist[5], mylist[6], mylist[7], mylist[8], mylist[9], mylist[10], mylist[11], mylist[12]))

db.commit()
c.close()










