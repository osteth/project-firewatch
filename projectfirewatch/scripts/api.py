from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
#FlaskAPI docs avilable at http://www.flaskapi.org/
import json

app = FlaskAPI(__name__)

@app.route("/api/", methods=['GET', 'POST'])
def Player_Checkin():
	'''
	curl -H "Content-Type: application/json" -X POST -d '{"TeamID": "Mudkips","IP": "192.168.0.1","Port": "5001"}' http://localhost:5001/checkin/
	'''
	try:
		checkin_resp = request.data
		IP = checkin_resp.get('IP')
		Port  = checkin_resp.get('Port')
		TeamID  = checkin_resp.get('TeamID')
		if IP and Port and TeamID is not None:
			Token, key = CheckinUpdate(IP, Port, TeamID)
			return {'Score Token': Token,
					'Key': key}
		else:
			return {'Invalid': 'request'}
	except:
		return {'Invalid': 'request'}


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)