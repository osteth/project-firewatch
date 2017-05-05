from flask_api import FlaskAPI, status, exceptions
from flask import request
from flask import jsonify


app = FlaskAPI(__name__)

@app.route("/ip", methods=["GET"])
def get_ip():
	return jsonify({'ip' : request.environ['REMOTE_ADDR']}), 200



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)



