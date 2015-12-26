import requests
import base64
import json
import time

TOKEN_URL = 'https://api.vasttrafik.se/token'
API_BASE_URL = 'https://api.vasttrafik.se/bin/rest.exe/v2'
FORMAT = '&format=json'

def fetchToken():
	f = open('credentials.txt', 'r')
	CONSUMER_KEY = f.readline().split('\'')[1]
	CONSUMER_SECRET = f.readline().split('\'')[1]

	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Authorization': 'Basic ' + base64.b64encode(CONSUMER_KEY + ':' + CONSUMER_SECRET)
	}
	data = {'grant_type': 'client_credentials'}

	response = requests.post(TOKEN_URL, data=data, headers=headers)
	obj = json.loads(response.content)
	return obj['access_token']

class Client:

	def __init__(self):
		self.token = fetchToken()

	def search_stops(self, query):
		data = self.get('/location.name?input=' + query + FORMAT)
		stopsArr = data['LocationList']['StopLocation']

		arr = []
		for stop in stopsArr:
			s = {}
			s['name'] = stop['name']
			s['id'] = stop['id']
			arr.append(s)
		return arr

	def get_departures(self, xstopID):
		return 'bar'

	def get(self, endpoint):
		url = API_BASE_URL + endpoint
		headers = {
			'Authorization': 'Bearer ' + self.token
		}
		res = requests.get(url, headers=headers)
		return json.loads(res.content, 'UTF-8')


# print '\n### API Client ###\n'

# query = raw_input('Where are you? ')
# fetchStopsUrl = API_URL + 'location.name?input=' + query + '&format=json'
# headers = {
# 	'Authorization': 'Bearer ' + access_token
# }
# response = requests.get(fetchStopsUrl, headers=headers)
# obj = json.loads(response.content, 'UTF-8')
# stopsArr = obj['LocationList']['StopLocation']

# print '\n## Results'
# for i in range(len(stopsArr)):
# 	stop = stopsArr[i]
# 	print stop['name'] + ' [' + str(i+1) + ']'

# index = raw_input('\nPlease choose your location: ')
# ID = stopsArr[int(index)]['id']
# fetchDeparturesUrl = API_URL + 'departureBoard?id=' + ID + '&date=' + time.strftime("%Y-%m-%d") + '&time=' + time.strftime("%H:%M") + '&format=json'

# response = requests.get(fetchDeparturesUrl, headers=headers)
# obj = json.loads(response.content, 'UTF-8')

# departuresArr = obj['DepartureBoard']['Departure']

# print '\n## Departures\n'
# for departure in departuresArr:
# 	print departure['name'] + ' --> ' + departure['direction'] + ' @ ' + departure['time'] + ' from track ' + departure['track']

# print '\n'