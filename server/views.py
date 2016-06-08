import json

from flask import Response, request
from server import app


@app.route('/success', methods = ['POST'])
def success():
	prettyPrint(request.data)
	return jsonOK()


@app.route('/failure', methods = ['POST'])
def failure():
	prettyPrint(request.data)
	return jsonOK()


@app.route('/notify', methods = ['POST'])
def notify():
	prettyPrint(request.data)
	return jsonOK()


@app.route('/interactive', methods = ['POST'])
def interactive():
	prettyPrint(request.data)
	return jsonOK()


@app.route('/destroy', methods = ['POST'])
def destroy():
	prettyPrint(request.data)
	return jsonOK()


def prettyPrint(requestBody):
	print('Calling endpoint: {ep}. Body ⤵'.format(ep = request.endpoint))

	jString = json.loads(requestBody.decode('utf-8'))
	print(json.dumps(jString, sort_keys = True, indent = 2))
	print()


def jsonOK():
	return Response(json.dumps({'status': 'OK'}),  mimetype='application/json')

