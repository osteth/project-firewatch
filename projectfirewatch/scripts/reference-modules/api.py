from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
#FlaskAPI docs avilable at http://www.flaskapi.org/
import json

app = FlaskAPI(__name__)

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




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)
