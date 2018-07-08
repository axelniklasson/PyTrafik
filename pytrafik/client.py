import requests
import base64
import json
import time as time_module

TOKEN_URL = 'https://api.vasttrafik.se/token'
API_BASE_URL = 'https://api.vasttrafik.se/bin/rest.exe/v2'
CONSUMER_KEY = '<YOUR_CONSUMER_KEY>'
CONSUMER_SECRET = '<YOUR_CONSUMER_SECRET>'

def fetchToken(key, secret):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Authorization': 'Basic ' + base64.b64encode((key + ':' + secret).encode()).decode()
	}
	data = {'grant_type': 'client_credentials'}

	response = requests.post(TOKEN_URL, data=data, headers=headers)
	obj = json.loads(response.content.decode('UTF-8'))
	return obj['access_token']

class Client:

	def __init__(self, format, key=CONSUMER_KEY, secret=CONSUMER_SECRET):
		self.token = fetchToken(key, secret)
		if format == 'JSON' or format == 'json':
			self.format = 'json'
		else:
			self.format = '' # defaulting to XML

	## /journeyDetail endpoint
	def get_journey_detail(self, ref, query_params=None):
		return ''

	## /location endpoint
	# /location.allstops
	def get_all_stops(self, query_params=None):
		data = self.get('/location.allstops')
		return data['LocationList']['StopLocation']

	# /location.nearbystops
	def get_nearby_stops(self, lat, long, query_params=None):
		data = self.get('/location.nearbystops?originCoordLat=' + str(lat) + '&originCoordLong=' + str(long))
		return data['LocationList']['StopLocation']

	# /location.name
	def get_stops_by_name(self, query, query_params=None):
		data = self.get('/location.name?input=' + query, query_params)
		return data['LocationList']['StopLocation']

	# /location.nearbyaddress
	def get_nearby_address(self, lat, long, query_params=None):
		data = self.get('/location.name?input=' + query, query_params)
		return data['LocationList']['CoordLocation']

	## /arrivalBoard endpoint
	def get_arrivals(self, stopID, date=None, time=None, query_params=None):
		if date is not None and time is not None:
			data = self.get('/arrivalBoard?id=' + str(stopID) + '&date=' + date + '&time=' + time, query_params)
		else:
			data = self.get('/arrivalBoard?id=' + str(stopID) + '&date=' + time_module.strftime("%Y-%m-%d") +
			'&time=' + time_module.strftime("%H:%M"), query_params)
		return data['ArrivalBoard']['Arrival']

	## /departureBoard endpoint
	def get_departures(self, stopID, date=None, time=None, query_params=None):
		if date is not None and time is not None:
			data = self.get('/departureBoard?id=' + str(stopID) + '&date=' + date + '&time=' + time, query_params)
		else:
			data = self.get('/departureBoard?id=' + str(stopID) + '&date=' + time_module.strftime("%Y-%m-%d") +
			'&time=' + time_module.strftime("%H:%M"), query_params)
		return data['DepartureBoard']['Departure']

	## /trip endpoint
	def calculate_trip(self, query_params=None):
		return ''

	## /livemap endpoint
	def get_livemap(self, longitudeMax, latitudeMax, longitudeMin, latitudeMin, onlyRealtime='yes', query_params=None):
		if longitudeMax is None or latitudeMax is None or longitudeMin is None or latitudeMin is None:
			raise Exception('Error: Missing argument!')
		data = self.get('/livemap?maxx=' + self.latlon_to_string_representation(longitudeMax) + '&maxy=' + self.latlon_to_string_representation(latitudeMax) + '&minx=' + self.latlon_to_string_representation(longitudeMin) + '&miny=' + self.latlon_to_string_representation(latitudeMin), query_params)
		return data['livemap']['vehicles']

	def latlon_to_string_representation(self, latlon):
		return str(round(latlon * 1000000)).rstrip('0').rstrip('.')

	## request builder
	def get(self, endpoint, query_params=None):
		url = API_BASE_URL + endpoint

		if query_params is not None:
			for key in query_params:
				url += '&' + key + '=' + query_params[key]
			url += '&format=' + self.format
		elif '?' in url:
			url += '&format=' + self.format
		else:
			url += '?format=' + self.format

		headers = {
			'Authorization': 'Bearer ' + self.token
		}
		res = requests.get(url, headers=headers)
		print (url)
		if res.status_code == 200:
			return json.loads(res.content.decode('UTF-8'))
		else:
			raise Exception('Error: ' + str(res.status_code) + str(res.content))
