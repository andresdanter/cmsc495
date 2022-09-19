#!/usr/bin/env python3

from flask import Flask, request, jsonify
from uuid import uuid4
from GetDirections import get_directions
from getRouteForcast import getTravelcast
from getRouteForcast import getForecast
from GetDirections import get_autocomplete
import dateutil.parser
import datetime
import pytz

app = Flask(__name__)

#rand_token = uuid4()
@app.route('/authToken')
def authToken():
	username = request.args.get('username', None)
	password = request.args.get('password', None)
	
	### Check user / pass against mySQL database
	
	if True:
		rand_token = uuid4()
		### Update database with randToken and token expiration
		return rand_token
	elif username == None or password == None:
		abort(400)
	else:
		abort(404)

@app.route('/addressSuggestions')
def addressSuggestions():
	address = request.args.get('address', None)
	return jsonify(get_autocomplete(address))

@app.route('/forecast')
def forecast():
	address = request.args.get('address', None)
	date = request.args.get('date', None)
	datePassed = request.args.get('datePassed', None)

	if datePassed == 'false':
		forecast = getForecast(address, None)
	else:
		forecast = getForecast(address, date)
		
	return jsonify(forecast)

@app.route('/travelcast')
def travelcast():
	addresses = request.args.get('addresses', None)
	addresses = addresses.split('|')
	date = dateutil.parser.parse(request.args.get('date', None))
	datePassed = request.args.get('datePassed', None)
	if datePassed == 'false':
		route = get_directions(addresses, datetime.datetime.now())['results']
		return jsonify(getTravelcast(route))
	else:
		route = get_directions(addresses, date)['results']
		return jsonify(getTravelcast(route))
	
if __name__ == '__main__':
	app.run(host='0.0.0.0')