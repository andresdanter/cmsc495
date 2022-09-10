#!/usr/bin/env python3

import requests
import datetime
import GetDirections

API_KEY = '92790be9ad93cd9fc5b49586e68d5331'

#	getRouteForcast Outputs the series of different forcasts to be experienced along the drive.
#	the route parameter is taken from the getDirections function dictionary result ['result']

#	Gets weather conditions of time closest to date d
def getNearestDate(d, date):
	temp = {}
	temp_time_diff = datetime.timedelta(days=1)
	for i in d['list']:
		timestamp = i['dt']
		date_compare = datetime.datetime.fromtimestamp(timestamp)
		
		if date_compare > date and date_compare - date < temp_time_diff:
			temp = i
			temp_time_diff = date_compare - date_compare
		if date >= date_compare and date - date_compare < temp_time_diff:
			temp = i
			temp_time_diff = date - date_compare
	
	return temp

#	Turns OpenWeatherAPI weather condition to a usable weather format
def parseWeather(weather, spec):
	if weather == 'Thunderstorm':
		if spec == 'thunderstorm with light rain' or spec == 'light thunderstorm' or spec == 'ragged thunderstorm' or spec == 'thunderstorm with light drizzle':
			return 'Thunderstorm', 'Light'
		elif spec == 'thunderstorm with rain' or spec == 'thunderstorm' or spec == 'thunderstorm with drizzle':
			return 'Thunderstorm', 'Normal'
		elif spec == 'thunderstorm with heavy rain' or spec == 'heavy thunderstorm' or spec == 'thunderstorm with heavy drizzle':
			return 'Thunderstorm', 'Heavy'
	
	if weather == 'Drizzle':
		if spec == 'light intensity drizzle' or spec == 'light intensity drizzle rain' or spec == 'shower drizzle':
			return 'Drizzle', 'Light'
		elif spec == 'drizzle' or spec == 'drizzle rain' or spec == 'shower rain and drizzle':
			return 'Drizzle', 'Normal'
		elif spec == 'heavy intensity drizzle' or spec == 'heavy intensity drizzle rain' or spec == 'heavy shower rain and drizzle':
			return 'Drizzle', 'Heavy'
	
	if weather == 'Rain':
		if spec == 'light rain' or spec == 'light intensity shower rain' or spec == 'ragged shower rain':
			return 'Rain', 'Light'
		elif spec == 'moderate rain' or spec == 'shower rain':
			return 'Rain', 'Moderate'
		elif spec == 'heavy intensity rain' or spec == 'heavy intensity shower rain':
			return 'Rain', 'Heavy'
		elif spec == 'very heavy rain' or spec == 'extreme rain':
			return 'Rain', 'Extreme'
		elif spec == 'freezing rain':
			return 'Rain', 'Freezing'
	
	if weather == 'Snow':
		if spec == 'light snow' or spec == 'light shower snow':
			return 'Snow', 'Light'
		elif spec == 'snow' or spec == 'shower snow':
			return 'Snow', 'Normal'
		elif spec == 'heavy snow' or spec == 'heavy shower snow':
			return 'Snow', 'Heavy'
		elif spec == 'light shower sleet' or spec == 'light rain and snow':
			return 'Sleet', 'Light'
		elif spec == 'shower sleet' or spec == 'rain and snow':
			return 'Sleet', 'Normal'
	
	if weather == 'Clear' or weather == 'Clouds':
		return 'Clear or Cloudy', 'Normal'
	
	if weather == 'Atmosphere' and spec == 'Tornado':
		return 'Tornado', 'Extreme'
	else:
		return 'Atmospheric Conditions', 'Light'
		

#	Gets aggregated weather conditions upon route (aggregated by weather)
#	Using 3-hour forcast until API access is approved
def getRouteForcast(route):
	results = []
	temp_weather_cond = ''
	temp_weather_name = ''
	start = route[0][0]
	for i in route:
	#	url = 'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API}'
		url = 'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API}'
		url = url.format(lat=i[1], lon=i[2], API=API_KEY)
		response = requests.get(url)
		json_data = response.json()
		weather = getNearestDate(json_data, i[0])
		weather_name = weather['weather'][0]['main']
		weather_cond = weather['weather'][0]['description']
		pw_name, pw_sev = parseWeather(weather_name, weather_cond)
		
		if temp_weather_cond == '':
			temp_weather_cond = pw_sev
			temp_weather_name = pw_name
		if temp_weather_cond != pw_sev:
			results.append([pw_name, pw_sev, start, i[0]])
			start = i[0]
			temp_weather_cond = pw_sev
			temp_weather_name = pw_name
	
	results.append([temp_weather_cond, start, i[0]])
	
	return results

route = GetDirections.get_directions('46346 Summerhill Pl., Sterling, VA 20165', '5511 Staunton Ave. SE, Charleston, WV 25304', datetime.datetime.now())['results']
print(getRouteForcast(route))