import requests
import base64
import json
import time as time_module

TOKEN_URL = 'https://api.vasttrafik.se/token'
API_BASE_URL = 'https://api.vasttrafik.se/bin/rest.exe/v2'

def fetchToken():
	f = open('code/credentials.txt', 'r')
	CONSUMER_KEY = f.readline().split('\'')[1]
	CONSUMER_SECRET = f.readline().split('\'')[1]

	headers = {
		'Content-qType': 'application/x-www-form-urlencoded',
		'Authorization': 'Basic ' + base64.b64encode(CONSUMER_KEY + ':' + CONSUMER_SECRET)
	}
	data = {'grant_type': 'client_credentials'}

	response = requests.post(TOKEN_URL, data=data, headers=headers)
	obj = json.loads(response.content)
	return obj['access_token']

class Client:

	def __init__(self, format):
		self.token = fetchToken()
		if format == 'JSON':
			self.format = '&format=json'
		else:
			# default is XML
			self.format = ''

	## /journeyDetail endpoint
	def get_journey_detail(self, ref, query_params=None):
		return ''

	## /location endpoint
	# /location.allstops
	def get_all_stops(self, query_params=None):
		return ''

	# /location.nearbystops
	def get_nearby_stops(self, lat, long, query_params=None):
		return ''

	# /location.name
	def get_stops_by_name(self, query, query_params=None):
		data = self.get('/location.name?input=' + query)
		return data['LocationList']['StopLocation']

	# /location.nearbyaddress
	def get_nearby_address(self, lat, long, query_params=None):
		return ''

	## /arrivalBoard endpoint
	def get_arrivals(self, stopID, date=None, time=None, query_params=None):
		if date is not None and time is not None:
			data = self.get('/arrivalBoard?id=' + str(stopID) + '&date=' + date + '&time=' + time)
		else:
			data = self.get('/arrivalBoard?id=' + str(stopID) + '&date=' + time_module.strftime("%Y-%m-%d") + 
			'&time=' + time_module.strftime("%H:%M"))
		return data['ArrivalBoard']['Arrival']

	## /departureBoard endpoint
	def get_departures(self, stopID, date=None, time=None, query_params=None):
		if date is not None and time is not None:
			data = self.get('/departureBoard?id=' + str(stopID) + '&date=' + date + '&time=' + time)
		else:
			data = self.get('/departureBoard?id=' + str(stopID) + '&date=' + time_module.strftime("%Y-%m-%d") + 
			'&time=' + time_module.strftime("%H:%M"))
		return data['DepartureBoard']['Departure']

	## /trip endpoint
	def calculate_trip(self, query_params=None):
		return ''

	## request builder
	def get(self, endpoint, query_params=None):
		url = API_BASE_URL + endpoint + self.format		

		if query_params is not None:
			for key in query_params:
				url += '&' + key + '=' + query_params[key]

		headers = {
			'Authorization': 'Bearer ' + self.token
		}

		res = requests.get(url, headers=headers)
		if res.status_code == 200:
			return json.loads(res.content, 'UTF-8')
		else:
			raise Exception('Error: ' + str(res.status_code) + res.read())
