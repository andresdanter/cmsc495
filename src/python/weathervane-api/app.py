#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from uuid import uuid4
from getDirections import get_directions
from getDirections import get_autocomplete
from getRouteForecast import getTravelcast
from getRouteForecast import getForecast
import dateutil.parser
import datetime
import pytz

app = Flask(__name__)
CORS(app,resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route('/addressSuggestions', methods = ['GET'])
@cross_origin(origin='*',headers=['content-type'])
def addressSuggestions():
    try:
        address = request.args.get('address', None)
        return jsonify(get_autocomplete(address))
    except:
        return jsonify([])

@app.route('/forecast', methods = ['GET'])
@cross_origin(origin='*',headers=['content-type'])
def forecast():
    
    address = request.args.get('address', None)
    date = request.args.get('date', None)
    datePassed = request.args.get('datePassed', None)

    if datePassed == 'false':
        forecast = getForecast(address, None)
    else:
        forecast = getForecast(address, date)
    print(forecast) 
    return jsonify(forecast)

@app.route('/travelcast', methods = ['GET'])
@cross_origin(origin='*',headers=['content-type'])
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
