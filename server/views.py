import json

from flask import Response
from server import app


@app.route('/success')
def success():
	return jsonOK()


@app.route('/failure')
def failure():
	return jsonOK()


@app.route('/notify')
def notify():
	return jsonOK()


@app.route('/interactive')
def interactive():
	return jsonOK()


@app.route('/destroy')
def destroy():
	return jsonOK()


def jsonOK():
	return Response(json.dumps({'status': 'OK'})),  mimetype='application/json')

